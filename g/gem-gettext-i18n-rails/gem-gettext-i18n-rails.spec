%define        gemname gettext_i18n_rails

Name:          gem-gettext-i18n-rails
Version:       1.10.0
Release:       alt1
Summary:       Simple FastGettext Rails integration
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/grosser/gettext_i18n_rails
Vcs:           https://github.com/grosser/gettext_i18n_rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bump) >= 0
BuildRequires: gem(gettext) >= 3.0.2
BuildRequires: gem(haml) >= 0
BuildRequires: gem(hamlit) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rails) >= 0
BuildRequires: gem(ruby_parser) >= 3.7.1
BuildRequires: gem(sexp_processor) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(slim) >= 0
BuildRequires: gem(sqlite3) >= 0
BuildRequires: gem(fast_gettext) >= 0.9.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names gettext_i18n_rails,gettext-i18n-rails
Requires:      gem(fast_gettext) >= 0.9.0
Obsoletes:     ruby-gettext_i18n_rails < %EVR
Provides:      ruby-gettext_i18n_rails = %EVR
Provides:      gem(gettext_i18n_rails) = 1.10.0


%description
FastGettext / Rails integration.

Translate via FastGettext, use any other I18n backend as
extension/fallback.

Rails does: I18n.t('syntax.with.lots.of.dots') with nested yml files We do:
_('Just translate my damn text!') with simple, flat mo/po/yml files or directly
from db. To use I18n calls add a syntax.with.lots.of.dots translation.


%package       -n gem-gettext-i18n-rails-doc
Version:       1.10.0
Release:       alt1
Summary:       Simple FastGettext Rails integration documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gettext_i18n_rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gettext_i18n_rails) = 1.10.0

%description   -n gem-gettext-i18n-rails-doc
Simple FastGettext Rails integration documentation files.

FastGettext / Rails integration.

Translate via FastGettext, use any other I18n backend as
extension/fallback.

Rails does: I18n.t('syntax.with.lots.of.dots') with nested yml files We do:
_('Just translate my damn text!') with simple, flat mo/po/yml files or directly
from db. To use I18n calls add a syntax.with.lots.of.dots translation.

%description   -n gem-gettext-i18n-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gettext_i18n_rails.


%package       -n gem-gettext-i18n-rails-devel
Version:       1.10.0
Release:       alt1
Summary:       Simple FastGettext Rails integration development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gettext_i18n_rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gettext_i18n_rails) = 1.10.0
Requires:      gem(bump) >= 0
Requires:      gem(gettext) >= 3.0.2
Requires:      gem(haml) >= 0
Requires:      gem(hamlit) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rails) >= 0
Requires:      gem(ruby_parser) >= 3.7.1
Requires:      gem(sexp_processor) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(slim) >= 0
Requires:      gem(sqlite3) >= 0

%description   -n gem-gettext-i18n-rails-devel
Simple FastGettext Rails integration development package.

FastGettext / Rails integration.

Translate via FastGettext, use any other I18n backend as
extension/fallback.

Rails does: I18n.t('syntax.with.lots.of.dots') with nested yml files We do:
_('Just translate my damn text!') with simple, flat mo/po/yml files or directly
from db. To use I18n calls add a syntax.with.lots.of.dots translation.

%description   -n gem-gettext-i18n-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gettext_i18n_rails.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-gettext-i18n-rails-doc
%ruby_gemdocdir

%files         -n gem-gettext-i18n-rails-devel


%changelog
* Thu Apr 13 2023 Pavel Skrylev <majioa@altlinux.org> 1.10.0-alt1
- ^ 1.8.1 -> 1.10.0

* Wed May 06 2020 Pavel Skrylev <majioa@altlinux.org> 1.8.1-alt1
- > Ruby Policy 2.0
- ^ 1.8.0 -> 1.8.1
- ! spec tags

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 1.8.0-alt1
- Initial gemified build for Sisyphus
