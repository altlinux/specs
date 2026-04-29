%define _unpackaged_files_terminate_build 1
%define  pkgname rbpdf
%define pkgfontname %pkgname-font
%define  pkgver 1.21.4
%define rbfontver 1.19.1

Name:    gem-%pkgname
Version: %pkgver
Release: alt1

Summary: Ruby on Rails TCPDF plugin
License: LGPL-2.1
Group:   Development/Ruby
Url:     https://github.com/naitoh/rbpdf
VCS:     https://github.com/naitoh/rbpdf.git

BuildArch: noarch

Source: gem-%pkgname-%pkgver.tar

BuildRequires(pre): rpm-macros-ruby
BuildRequires: rpm-build-ruby

%description
A template plugin allowing the inclusion of ERB-enabled RBPDF template files.

%package doc
Summary: Documentation files for %name gem
Group: Development/Documentation
BuildArch: noarch

%description doc
Documentation files for %{name}.

%package -n gem-%pkgfontname
Summary: Fonts for gem-%name
Version: %rbfontver
Group: Other
BuildArch: noarch

%description -n gem-%pkgfontname
%summary

%package -n gem-%pkgfontname-doc
Summary: Documentation files for %name gem
Version: %rbfontver
Group: Development/Documentation
BuildArch: noarch

%description -n gem-%pkgfontname-doc
%summary

%prep
%setup

%build
%ruby_build

%install
%ruby_install

rm -rf %buildroot%ruby_gemslibdir/%pkgfontname-%rbfontver/lib/fonts/ttf2ufm

%check
%ruby_test

%files
%doc *.md
%ruby_gemslibdir/%pkgname-%pkgver
%ruby_gemspecdir/%pkgname-%pkgver.gemspec

%files -n gem-%pkgfontname
%ruby_gemslibdir/%pkgfontname-%rbfontver
%ruby_gemspecdir/%pkgfontname-%rbfontver.gemspec

%files doc
%ruby_gemsdocdir/%pkgname-%{pkgver}*

%files -n gem-%pkgfontname-doc
%ruby_gemsdocdir/%pkgfontname-%{rbfontver}*

%changelog
* Tue Apr 28 2026 Artem Semenov <savoptik@altlinux.org> 1.21.4-alt1
- Initial build for Sisyphus
