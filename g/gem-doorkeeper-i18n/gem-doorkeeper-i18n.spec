%define _unpackaged_files_terminate_build 1
%define  pkgname doorkeeper-i18n

Name: gem-%pkgname
Version: 5.2.6
Release: alt1

Summary: Translation files for Doorkeeper OAuth 2 provider  
License: MIT
Group: Development/Ruby
Url: https://github.com/doorkeeper-gem/doorkeeper-i18n
VCS: https://github.com/doorkeeper-gem/doorkeeper-i18n 
BuildArch: noarch

Source: %pkgname-%version.tar

BuildRequires(pre): rpm-macros-ruby
BuildRequires: rpm-build-ruby

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
%_logdir/doorkeeper-i18n

%files doc
%ruby_gemdocdir

%changelog
* Tue Apr 28 2026 Aleksandr Dovydenkov <asd@altlinux.org> 5.2.6-alt1
- Initial build for ALT Linux.
