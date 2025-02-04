%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname po_to_json

Name:          gem-po-to-json
Version:       1.1.0
Release:       alt1
Summary:       Convert gettext PO files to JSON objects so that you can use it in your application
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/webhippie/po_to_json
Vcs:           https://github.com/webhippie/po_to_json.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(json) >= 1.6.0
BuildRequires: gem(listen) >= 3.0.7
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
%ruby_alias_names po_to_json,po-to-json
Requires:      ruby >= 1.9.3
Requires:      gem(json) >= 1.6.0
Provides:      po_to_json = %EVR
Provides:      gem(po_to_json) = 1.1.0

%description
Convert gettext PO files to JSON to use in your javascript app, based on
po2json.pl by DuckDuckGo, Inc.. Ideally you'll use this on a Rake task that
creates JSON versions of your PO files, which can later be used from javascript
with Jed.


%if_enabled    doc
%package       -n gem-po-to-json-doc
Version:       1.1.0
Release:       alt1
Summary:       Convert gettext PO files to JSON objects so that you can use it in your application documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета po_to_json
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(po_to_json) = 1.1.0

%description   -n gem-po-to-json-doc
Convert gettext PO files to JSON objects so that you can use it in your
application documentation files.

Convert gettext PO files to JSON to use in your javascript app, based on
po2json.pl by DuckDuckGo, Inc.. Ideally you'll use this on a Rake task that
creates JSON versions of your PO files, which can later be used from javascript
with Jed.

%description   -n gem-po-to-json-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета po_to_json.
%endif


%if_enabled    devel
%package       -n gem-po-to-json-devel
Version:       1.1.0
Release:       alt1
Summary:       Convert gettext PO files to JSON objects so that you can use it in your application development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета po_to_json
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(po_to_json) = 1.1.0
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

%description   -n gem-po-to-json-devel
Convert gettext PO files to JSON objects so that you can use it in your
application development package.

Convert gettext PO files to JSON to use in your javascript app, based on
po2json.pl by DuckDuckGo, Inc.. Ideally you'll use this on a Rake task that
creates JSON versions of your PO files, which can later be used from javascript
with Jed.

%description   -n gem-po-to-json-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета po_to_json.
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
%files         -n gem-po-to-json-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-po-to-json-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Mon Jan 13 2025 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- ^ 1.0.1.1 -> 1.1.0

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.1.1-alt0.1
- ^ 1.0.1 -> 1.0.1[.1]

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
