%define  pkgname rhcl

Name:    gem-%pkgname
Version: 0.1.0
Release: alt1

Summary: Pure Ruby HCL parser
License: MIT
Group:   Development/Ruby
Url:     https://github.com/winebarrel/rhcl

BuildArch: noarch

Source: %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
%summary.

%package doc
Summary: Documentation files for %name gem
Group: Development/Documentation
BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc *.md
%ruby_gemspec
%ruby_gemlibdir

%files doc
%ruby_gemdocdir

%changelog
* Tue Jun 30 2026 Alexander Burmatov <thatman@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus.
