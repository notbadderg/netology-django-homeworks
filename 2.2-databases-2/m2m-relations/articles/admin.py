from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ArticleInlineFormset(BaseInlineFormSet):
    def clean(self):
        quantity_of_main_scopes = 0
        for form in self.forms:
            data = form.cleaned_data
            print(data)
            if data.get('is_main'):
                quantity_of_main_scopes += 1
                if data.get('DELETE'):
                    quantity_of_main_scopes -= 1
        if quantity_of_main_scopes == 1:
            return super().clean()
        elif quantity_of_main_scopes < 1:
            raise ValidationError('Укажите основной раздел '
                                  '(в результате сохранения статья останется без основного раздела)')
        else:
            raise ValidationError('Основным может быть только один раздел '
                                  '(в результате сохранения у статьи станет больше одного раздела)')


class ArticleInline(admin.TabularInline):
    model = Scope
    formset = ArticleInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleInline]


@admin.register(Tag)
class ArticleAdmin(admin.ModelAdmin):
    pass
