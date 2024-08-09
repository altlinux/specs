%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname trenni

Name:          gem-trenni
Version:       3.14.0
Release:       alt1
Summary:       A fast native templating system that compiles directly to Ruby code
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ioquatix/trenni
Vcs:           https://github.com/ioquatix/trenni.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bake) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(covered) >= 0
BuildRequires: gem(rspec) >= 3.4
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(trenni) = 3.14.0


%description
Trenni is a templating system built loosely on top of XHTML markup. It uses
efficient native parsers where possible and compiles templates into efficient
Ruby. It also includes a markup builder to assist with the generation of
pleasantly formatted markup which is compatible with the included parsers.


%if_enabled    doc
%package       -n gem-trenni-doc
Version:       3.14.0
Release:       alt1
Summary:       A fast native templating system that compiles directly to Ruby code documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета trenni
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(trenni) = 3.14.0

%description   -n gem-trenni-doc
A fast native templating system that compiles directly to Ruby code
documentation files.

Trenni is a templating system built loosely on top of XHTML markup. It uses
efficient native parsers where possible and compiles templates into efficient
Ruby. It also includes a markup builder to assist with the generation of
pleasantly formatted markup which is compatible with the included parsers.

%description   -n gem-trenni-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета trenni.
%endif


%if_enabled    devel
%package       -n gem-trenni-devel
Version:       3.14.0
Release:       alt1
Summary:       A fast native templating system that compiles directly to Ruby code development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета trenni
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(trenni) = 3.14.0
Requires:      gem(bake) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(covered) >= 0
Requires:      gem(rspec) >= 3.4
Conflicts:     gem(rspec) >= 4

%description   -n gem-trenni-devel
A fast native templating system that compiles directly to Ruby code development
package.

Trenni is a templating system built loosely on top of XHTML markup. It uses
efficient native parsers where possible and compiles templates into efficient
Ruby. It also includes a markup builder to assist with the generation of
pleasantly formatted markup which is compatible with the included parsers.

%description   -n gem-trenni-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета trenni.
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
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-trenni-doc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-trenni-devel
%ruby_includedir/*
%endif


%changelog
* Fri Jul 26 2024 Pavel Skrylev <majioa@altlinux.org> 3.14.0-alt1
- ^ 3.13.1 -> 3.14.0

* Mon Oct 17 2022 Pavel Skrylev <majioa@altlinux.org> 3.13.1-alt1
- + packaged gem with Ruby Policy 2.0
