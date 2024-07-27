Name: fonts-ttf-cascadia-code
Version: 2404.23
Release: alt1

Summary: A fun new coding TTF font that comes bundled with Windows Terminal 
License: OFL-1.1
Group: System/Fonts/True type
Url: https://devblogs.microsoft.com/commandline/cascadia-code/
Source: CascadiaCode-%version.zip
Obsoletes: fonts-cascadia-code
Provides: fonts-cascadia-code = 30000

BuildArch: noarch
BuildRequires: rpm-build-fonts unzip

%description
Cascadia is a fun new coding font that comes bundled with Windows
Terminal, and is now the default font in Visual Studio as well.

%package -n fonts-otf-cascadia-code
Group: System/Fonts/True type
Summary: A fun new coding OTF font that comes bundled with Windows Terminal 
%description -n fonts-otf-cascadia-code
Cascadia is a fun new coding font that comes bundled with Windows
Terminal, and is now the default font in Visual Studio as well.

%prep
%setup -c

%build
%install
cd ttf && %ttf_fonts_install Cascadia
cd ..
cd otf/static && %otf_fonts_install Cascadia

%files -f ttf/Cascadia.files

%files -n fonts-otf-cascadia-code -f otf/static/Cascadia.files

%changelog
* Sat Jul 27 2024 Fr. Br. George <george@altlinux.org> 2404.23-alt1
- Rename according to font policy
- Introduce OTF version
- Autobuild version bump to 2404.23 (Closes: #49429)

* Thu Sep 19 2019 Fr. Br. George <george@altlinux.ru> 21909.16-alt1
- Initial build for ALT

