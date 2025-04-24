%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname therubyracer

Name:          gem-therubyracer
Version:       0.12.3.10
Release:       alt0.1
Summary:       Embed the V8 JavaScript interpreter into Ruby
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/cowboyd/therubyracer
Vcs:           https://github.com/cowboyd/therubyracer.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gcc-c++
BuildRequires: node-devel
#BuildRequires: libv8-3.14-devel
%if_enabled check
BuildRequires: gem(libv8) >= 3.16.14.15
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(redjs) >= 0
BuildRequires: gem(ref) >= 0
BuildRequires: gem(rspec) >= 3.5.0
BuildConflicts: gem(libv8) >= 9
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency libv8 >= 8.4.255.0,libv8 < 9
Requires:      gem(libv8) >= 3.16.14.15
Requires:      gem(ref) >= 0
Conflicts:     gem(libv8) >= 9
Provides:      gem(therubyracer) = 0.12.3.10

%ruby_use_gem_version therubyracer:0.12.3.10

%description
Call JavaScript code and manipulate JavaScript objects from Ruby. Call Ruby code
and manipulate Ruby objects from JavaScript.


%if_enabled    doc
%package       -n gem-therubyracer-doc
Version:       0.12.3.10
Release:       alt0.1
Summary:       Embed the V8 JavaScript interpreter into Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета therubyracer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(therubyracer) = 0.12.3.10

%description   -n gem-therubyracer-doc
Embed the V8 JavaScript interpreter into Ruby documentation files.

Call JavaScript code and manipulate JavaScript objects from Ruby. Call Ruby code
and manipulate Ruby objects from JavaScript.

%description   -n gem-therubyracer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета therubyracer.
%endif


%if_enabled    devel
%package       -n gem-therubyracer-devel
Version:       0.12.3.10
Release:       alt0.1
Summary:       Embed the V8 JavaScript interpreter into Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета therubyracer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(therubyracer) = 0.12.3.10
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(redjs) >= 0
Requires:      gem(rspec) >= 3.5.0
Conflicts:     gem(rspec) >= 4

%description   -n gem-therubyracer-devel
Embed the V8 JavaScript interpreter into Ruby development package.

Call JavaScript code and manipulate JavaScript objects from Ruby. Call Ruby code
and manipulate Ruby objects from JavaScript.

%description   -n gem-therubyracer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета therubyracer.
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
%doc Changelog.md README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-therubyracer-doc
%doc Changelog.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-therubyracer-devel
%doc Changelog.md README.md
%ruby_includedir/*
%endif


%changelog
* Fri Dec 13 2024 Pavel Skrylev <majioa@altlinux.org> 0.12.3.10-alt0.1
- ^ 0.12.3 -> 0.12.3p10
- ! NMU: just workaround, not real fix

* Sat Dec 02 2023 Pavel Skrylev <majioa@altlinux.org> 0.12.3-alt1
- + packaged gem with Ruby Policy 2.0 without devel
