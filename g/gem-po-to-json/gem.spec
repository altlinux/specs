%define        gemname po_to_json

Name:          gem-po-to-json
Version:       1.0.1.1
Release:       alt0.1
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
BuildRequires: gem(rake) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(json) >= 1.6.0 gem(json) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency json >= 2.3.0,json < 3
%ruby_alias_names po_to_json,po-to-json
%ruby_use_gem_version po_to_json:1.0.1.1
Requires:      gem(json) >= 1.6.0 gem(json) < 3
Provides:      gem(po_to_json) = 1.0.1.1


%description
Convert gettext PO files to JSON to use in your javascript app, based on
po2json.pl by DuckDuckGo, Inc.. Ideally you'll use this on a Rake task that
creates JSON versions of your PO files, which can later be used from javascript
with Jed.


%package       -n gem-po-to-json-doc
Version:       1.0.1.1
Release:       alt0.1
Summary:       Convert gettext PO files to JSON objects so that you can use it in your application documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета po_to_json
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(po_to_json) = 1.0.1.1

%description   -n gem-po-to-json-doc
Convert gettext PO files to JSON objects so that you can use it in your
application documentation files.

Convert gettext PO files to JSON to use in your javascript app, based on
po2json.pl by DuckDuckGo, Inc.. Ideally you'll use this on a Rake task that
creates JSON versions of your PO files, which can later be used from javascript
with Jed.

%description   -n gem-po-to-json-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета po_to_json.


%package       -n gem-po-to-json-devel
Version:       1.0.1.1
Release:       alt0.1
Summary:       Convert gettext PO files to JSON objects so that you can use it in your application development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета po_to_json
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(po_to_json) = 1.0.1.1
Requires:      gem(bundler) >= 0 gem(bundler) < 3
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(yard) >= 0
Requires:      gem(rspec) >= 0 gem(rspec) < 4

%description   -n gem-po-to-json-devel
Convert gettext PO files to JSON objects so that you can use it in your
application development package.

Convert gettext PO files to JSON to use in your javascript app, based on
po2json.pl by DuckDuckGo, Inc.. Ideally you'll use this on a Rake task that
creates JSON versions of your PO files, which can later be used from javascript
with Jed.

%description   -n gem-po-to-json-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета po_to_json.


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

%files         -n gem-po-to-json-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-po-to-json-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.1.1-alt0.1
- ^ 1.0.1 -> 1.0.1[.1]

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
