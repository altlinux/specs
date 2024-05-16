%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname erb

Name:          gem-erb
Version:       4.0.4
Release:       alt1
Summary:       An easy to use but powerful templating system for Ruby
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/erb
Vcs:           https://github.com/ruby/erb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(test-unit-ruby-core) >= 0
BuildRequires: gem(cgi) >= 0.3.3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(cgi) >= 0.3.3
Provides:      gem(erb) = 4.0.4


%description
An easy to use but powerful templating system for Ruby.


%package       -n erb
Version:       4.0.4
Release:       alt1
Summary:       An easy to use but powerful templating system for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета erb
Group:         Other
BuildArch:     noarch

Requires(pre): alternatives >= 0:0.2.0-alt0.12
Requires:      gem(erb) = 4.0.4

%description   -n erb
An easy to use but powerful templating system for Ruby executable(s).

%description   -n erb -l ru_RU.UTF-8
Исполнямка для самоцвета erb.


%if_enabled    doc
%package       -n gem-erb-doc
Version:       4.0.4
Release:       alt1
Summary:       An easy to use but powerful templating system for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета erb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(erb) = 4.0.4

%description   -n gem-erb-doc
An easy to use but powerful templating system for Ruby documentation files.

%description   -n gem-erb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета erb.
%endif


%if_enabled    devel
%package       -n gem-erb-devel
Version:       4.0.4
Release:       alt1
Summary:       An easy to use but powerful templating system for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета erb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(erb) = 4.0.4
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(test-unit-ruby-core) >= 0

%description   -n gem-erb-devel
An easy to use but powerful templating system for Ruby development package.

%description   -n gem-erb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета erb.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

rm -rf %buildroot%_bindir/erb
mkdir -p %buildroot%_altdir/
cat <<EOF >>%buildroot%_altdir/erb
%{_bindir}/erb %ruby_gemlibdir/exe/erb 100
EOF

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n erb
%doc README.md
%_altdir/erb

%if_enabled    doc
%files         -n gem-erb-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-erb-devel
%doc README.md
%endif


%changelog
* Sun Apr 21 2024 Pavel Skrylev <majioa@altlinux.org> 4.0.4-alt1
- + packaged gem with Ruby Policy 2.0
