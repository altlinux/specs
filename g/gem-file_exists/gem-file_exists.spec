%define gemname file_exists

Name: gem-%gemname
Version: 0.2.0
Release: alt1

Summary: File/Dir.exists implementation for Ruby >= 3.2
License: Unlicense
Group: Development/Ruby
Url: https://rubygems.org/gems/file_exists

Vcs: https://github.com/largo/file_exists

BuildArch: noarch

Source: https://github.com/Largo/file_exists/archive/v%version/%gemname-%version.tar.gz

BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rspec) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides: gem(childlabor) = 0.0.3

%description
File.exists? and Dir.exists? were deprecated in Ruby 3.2. If you still
need these methods. just require this Gem.

%package doc
Summary: %gemname documentation files
Group: Development/Documentation
BuildArch: noarch
Requires: %name = %EVR

%description doc
This package provides %gemname documentation files.

%prep
%setup -n %gemname-%version

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir
%doc README* CHANGELOG*

%files doc
%ruby_gemdocdir

%changelog
* Wed Aug 14 2024 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for Sisyphus
