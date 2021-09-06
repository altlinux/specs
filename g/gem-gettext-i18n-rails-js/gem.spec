%define        gemname gettext_i18n_rails_js

Name:          gem-gettext-i18n-rails-js
Version:       1.3.0.1
Release:       alt0.1
Summary:       Extends gettext_i18n_rails making your .PO files available to client side javascript as JSON
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/webhippie/gettext_i18n_rails_js
Vcs:           https://github.com/webhippie/gettext_i18n_rails_js.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rails) >= 3.2.0
BuildRequires: gem(gettext) >= 3.0.2
BuildRequires: gem(gettext_i18n_rails) >= 0.7.1
BuildRequires: gem(po_to_json) >= 1.0.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_version gettext_i18n_rails_js:1.3.0.1
%ruby_alias_names gettext_i18n_rails_js,gettext-i18n-rails-js
Requires:      gem(rails) >= 3.2.0
Requires:      gem(gettext) >= 3.0.2
Requires:      gem(gettext_i18n_rails) >= 0.7.1
Requires:      gem(po_to_json) >= 1.0.0
Provides:      gem(gettext_i18n_rails_js) = 1.3.0.1


%description
Extends gettext_i18n_rails, making your .PO files available to client side
javascript as JSON. It will find translations inside your .js, .coffee,
.handlebars and .mustache files, then it will create JSON versions of your .PO
files so you can serve them with the rest of your assets, thus letting you
access all your translations offline from client side javascript.


%package       -n gem-gettext-i18n-rails-js-doc
Version:       1.3.0.1
Release:       alt0.1
Summary:       Extends gettext_i18n_rails making your .PO files available to client side javascript as JSON documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gettext_i18n_rails_js
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gettext_i18n_rails_js) = 1.3.0.1

%description   -n gem-gettext-i18n-rails-js-doc
Extends gettext_i18n_rails making your .PO files available to client side
javascript as JSON documentation files.

Extends gettext_i18n_rails, making your .PO files available to client side
javascript as JSON. It will find translations inside your .js, .coffee,
.handlebars and .mustache files, then it will create JSON versions of your .PO
files so you can serve them with the rest of your assets, thus letting you
access all your translations offline from client side javascript.

%description   -n gem-gettext-i18n-rails-js-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gettext_i18n_rails_js.


%package       -n gem-gettext-i18n-rails-js-devel
Version:       1.3.0.1
Release:       alt0.1
Summary:       Extends gettext_i18n_rails making your .PO files available to client side javascript as JSON development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gettext_i18n_rails_js
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gettext_i18n_rails_js) = 1.3.0.1
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(rspec) >= 0

%description   -n gem-gettext-i18n-rails-js-devel
Extends gettext_i18n_rails making your .PO files available to client side
javascript as JSON development package.

Extends gettext_i18n_rails, making your .PO files available to client side
javascript as JSON. It will find translations inside your .js, .coffee,
.handlebars and .mustache files, then it will create JSON versions of your .PO
files so you can serve them with the rest of your assets, thus letting you
access all your translations offline from client side javascript.

%description   -n gem-gettext-i18n-rails-js-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gettext_i18n_rails_js.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-gettext-i18n-rails-js-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-gettext-i18n-rails-js-devel
%doc README.md


%changelog
* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.0.1-alt0.1
- ^ 1.3.0 -> 1.3.0[.1]

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
