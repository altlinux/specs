%define _unpackaged_files_terminate_build 1
%define pkgname actionpack-xml_parser

Name: gem-%pkgname
Version: 2.0.1
Release: alt1

Summary: XML parameters parser for Action Pack (removed from core in Rails 4.0)  
License: MIT
Group: Development/Ruby
Url: https://github.com/rails/actionpack-xml_parser
VCS: https://github.com/rails/actionpack-xml_parser
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

%files doc
%ruby_gemdocdir

%changelog
* Tue Apr 28 2026 Aleksandr Dovydenkov <asd@altlinux.org> 2.0.1-alt1
- Initial build for ALT Linux.
