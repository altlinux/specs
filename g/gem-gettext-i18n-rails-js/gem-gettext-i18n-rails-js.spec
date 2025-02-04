%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname gettext_i18n_rails_js

Name:          gem-gettext-i18n-rails-js
Version:       1.4.0
Release:       alt1
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
BuildRequires: gem(gettext) >= 3.0.2
BuildRequires: gem(gettext_i18n_rails) >= 0.7.1
BuildRequires: gem(listen) >= 3.0.7
BuildRequires: gem(po_to_json) >= 1.0.0
BuildRequires: gem(rails) >= 3.2.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(yard) >= 0
%if_enabled check
BuildRequires: gem(guard) >= 0
BuildRequires: gem(guard-rspec) >= 0
BuildRequires: gem(guard-rubocop) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(simplecov) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names gettext_i18n_rails_js,gettext-i18n-rails-js
Requires:      ruby >= 1.9.3
Requires:      gem(gettext) >= 3.0.2
Requires:      gem(gettext_i18n_rails) >= 0.7.1
Requires:      gem(po_to_json) >= 1.0.0
Requires:      gem(rails) >= 3.2.0
Provides:      gettext_i18n_rails_js = %EVR
Provides:      gem(gettext_i18n_rails_js) = 1.4.0

%description
Extends gettext_i18n_rails, making your .PO files available to client side
javascript as JSON. It will find translations inside your .js, .coffee,
.handlebars and .mustache files, then it will create JSON versions of your .PO
files so you can serve them with the rest of your assets, thus letting you
access all your translations offline from client side javascript.


%if_enabled    doc
%package       -n gem-gettext-i18n-rails-js-doc
Version:       1.4.0
Release:       alt1
Summary:       Extends gettext_i18n_rails making your .PO files available to client side javascript as JSON documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gettext_i18n_rails_js
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gettext_i18n_rails_js) = 1.4.0

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
%endif


%if_enabled    devel
%package       -n gem-gettext-i18n-rails-js-devel
Version:       1.4.0
Release:       alt1
Summary:       Extends gettext_i18n_rails making your .PO files available to client side javascript as JSON development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gettext_i18n_rails_js
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gettext_i18n_rails_js) = 1.4.0
Requires:      gem(bundler) >= 0
Requires:      gem(guard) >= 0
Requires:      gem(guard-rspec) >= 0
Requires:      gem(guard-rubocop) >= 0
Requires:      gem(listen) >= 3.0.7
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(yard) >= 0

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
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc CHANGELOG.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-gettext-i18n-rails-js-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-gettext-i18n-rails-js-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Mon Jan 13 2025 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1
- ^ 1.3.1.1 -> 1.4.0

* Fri Oct 07 2022 Pavel Skrylev <majioa@altlinux.org> 1.3.1.1-alt0.1
- ^ 1.3.1 -> 1.3.1[1]

* Thu Sep 15 2022 Pavel Skrylev <majioa@altlinux.org> 1.3.1-alt1
- ^ 1.3.0.1 -> 1.3.1

* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.0.1-alt0.1
- ^ 1.3.0 -> 1.3.0[.1]

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
