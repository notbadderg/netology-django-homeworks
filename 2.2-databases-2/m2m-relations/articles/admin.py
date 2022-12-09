from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ArticleInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_scope_selected = False
        for form in self.forms:
            data = form.cleaned_data
            if data.get('is_main'):
                if is_main_scope_selected:
                    raise ValidationError('Основным может быть только один раздел')
                else:
                    is_main_scope_selected = True
        if not is_main_scope_selected:
            raise ValidationError('Укажите основной раздел')
        return super().clean()


class ArticleInline(admin.TabularInline):
    model = Scope
    formset = ArticleInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleInline]


@admin.register(Tag)
class ArticleAdmin(admin.ModelAdmin):
    pass
