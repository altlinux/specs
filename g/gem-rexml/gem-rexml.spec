%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rexml

Name:          gem-rexml
Version:       3.3.2
Release:       alt1
Summary:       REXML is an XML toolkit for Ruby
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/rexml
Vcs:           https://github.com/ruby/rexml.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(benchmark_driver) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(test-unit-ruby-core) >= 0
BuildRequires: gem(strscan) >= 3.1.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(strscan) >= 0
Provides:      gem(rexml) = 3.3.2


%description
REXML was inspired by the Electric XML library for Java, which features an
easy-to-use API, small size, and speed. Hopefully, REXML, designed with the same
philosophy, has these same features. I've tried to keep the API as intuitive as
possible, and have followed the Ruby methodology for method naming and code
flow, rather than mirroring the Java API.

REXML supports both tree and stream document parsing. Stream parsing is faster
(about 1.5 times as fast). However, with stream parsing, you don't get access to
features such as XPath.


%if_enabled    doc
%package       -n gem-rexml-doc
Version:       3.3.2
Release:       alt1
Summary:       REXML is an XML toolkit for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rexml
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rexml) = 3.3.2

%description   -n gem-rexml-doc
REXML is an XML toolkit for Ruby documentation files.

REXML was inspired by the Electric XML library for Java, which features an
easy-to-use API, small size, and speed. Hopefully, REXML, designed with the same
philosophy, has these same features. I've tried to keep the API as intuitive as
possible, and have followed the Ruby methodology for method naming and code
flow, rather than mirroring the Java API.

REXML supports both tree and stream document parsing. Stream parsing is faster
(about 1.5 times as fast). However, with stream parsing, you don't get access to
features such as XPath.

%description   -n gem-rexml-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rexml.
%endif


%if_enabled    devel
%package       -n gem-rexml-devel
Version:       3.3.2
Release:       alt1
Summary:       REXML is an XML toolkit for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rexml
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rexml) = 3.3.2
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(benchmark_driver) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(test-unit-ruby-core) >= 0

%description   -n gem-rexml-devel
REXML is an XML toolkit for Ruby development package.

REXML was inspired by the Electric XML library for Java, which features an
easy-to-use API, small size, and speed. Hopefully, REXML, designed with the same
philosophy, has these same features. I've tried to keep the API as intuitive as
possible, and have followed the Ruby methodology for method naming and code
flow, rather than mirroring the Java API.

REXML supports both tree and stream document parsing. Stream parsing is faster
(about 1.5 times as fast). However, with stream parsing, you don't get access to
features such as XPath.

%description   -n gem-rexml-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rexml.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rexml-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rexml-devel
%doc README.md
%endif


%changelog
* Tue Jul 23 2024 Pavel Skrylev <majioa@altlinux.org> 3.3.2-alt1
- ^ 3.2.8 -> 3.3.2

* Fri May 24 2024 Pavel Skrylev <majioa@altlinux.org> 3.2.8-alt1
- ^ 3.2.5 -> 3.2.8

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 3.2.5-alt1
- ^ 3.2.4 -> 3.2.5

* Mon Jul 14 2020 Pavel Skrylev <majioa@altlinux.org> 3.2.4-alt1
- + packaged gem with usage Ruby Policy 2.0
