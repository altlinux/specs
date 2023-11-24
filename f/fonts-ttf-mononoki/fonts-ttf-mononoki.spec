%define origname mononoki

Name: fonts-ttf-%origname
Version: 1.6
Release: alt1

Summary: A font for programming and code review
Group: System/Fonts/True type
License: OFL-1.1

Url: https://github.com/madmalik/%origname
# Source-url: %url/releases/download/%version/%origname.zip
Source: %name-%version.tar.gz

BuildArch: noarch
BuildRequires: rpm-build-fonts

%description
Mononoki is a typeface created to enhance code formatting.  It works well on
both high and low resolution displays. Every character is clearly
distinguishable from similar looking characters.

%prep
%setup

%install
mkdir -p %buildroot%_ttffontsdir/%origname/
install -m644 *.ttf %buildroot%_ttffontsdir/%origname/

%files
%_ttffontsdir/%origname/

%changelog
* Fri Nov 24 2023 Anton Zhukharev <ancieg@altlinux.org> 1.6-alt1
- (NMU) Updated to 1.6.

* Sun Jun 17 2018 Elvira Khabirova <lineprinter@altlinux.org> 1.2-alt1
- Initial build
