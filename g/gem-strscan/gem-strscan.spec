%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%def_disable   java
%define        gemname strscan

Name:          gem-strscan
Version:       3.1.1
Release:       alt0.1
Summary:       Provides lexical scanning operations on a String
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/strscan
Vcs:           https://github.com/ruby/strscan.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(benchmark-driver) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(test-unit-ruby-core) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(strscan) = 3.1.1


%description
Provides lexical scanning operations on a String.


%if_enabled    devel
%package       -n gem-strscan-devel
Version:       3.1.1
Release:       alt0.1
Summary:       Provides lexical scanning operations on a String development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета strscan
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(strscan) = 3.1.1
Requires:      gem(benchmark-driver) >= 0
Requires:      gem(rake-compiler) >= 0
%{?_enable_java:Requires: gem(ruby-maven) >= 0}
Requires:      gem(test-unit) >= 0
Requires:      gem(test-unit-ruby-core) >= 0

%description   -n gem-strscan-devel
Provides lexical scanning operations on a String development package.

%description   -n gem-strscan-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета strscan.
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

%if_enabled    devel
%files         -n gem-strscan-devel
%endif


%changelog
* Fri May 24 2024 Pavel Skrylev <majioa@altlinux.org> 3.1.1-alt0.1
- + packaged gem with Ruby Policy 2.0
