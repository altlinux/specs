# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Summary: Extrema is a powerful visualization and data analysis tool
Name: extrema
Version: 4.4.5
Release: alt3
License: GPLv2+
Packager: Ilya Mashkin <oddity@altlinux.ru>
Group: Engineering
Url: http://exsitewebware.com/extrema/
Source0: http://downloads.sourceforge.net/extrema/extrema-%version.tar.gz
Patch0: extrema-4.2.10.desktop.patch
Patch1: extrema-4.4.5-gcc46.patch
Patch2: extrema-4.4.5-alt-gcc8.patch
BuildRequires: wxGTK-devel >= 2.6.3
BuildRequires: desktop-file-utils
BuildRequires: ImageMagick
Requires: extrema-help
Source44: import.info

%description
Extrema is a powerful visualization and data analysis tool that
enables researchers to quickly distill their large, complex data sets
into meaningful information. Its flexibility, sophistication, and
power allow you to easily develop your own commands and create highly
customized graphs.

%package help
Summary: Help files for Extrema
Group: Engineering
BuildArch: noarch
Requires: %name = %version-%release

%description help
This package contains help files for Extrema.

%package doc
Summary: Extrema documentation in PDF format
Group: Engineering
BuildArch: noarch
Requires: %name = %version-%release

%description doc
This package contains Getting Started, User Guide and other
documentation in PDF format for Extrema.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p2

%build
%configure --disable-static
%__make %{?_smp_mflags}
convert Images/%name.gif %name.png

%install
%__make install DESTDIR=%buildroot
desktop-file-install \
    --dir=%buildroot%_datadir/applications %name.desktop
%__install -m 0644 -D %name.png %buildroot%_datadir/pixmaps/%name.png
%__rm -f %buildroot%_libdir/lib%name.{la,a}

%files
%doc AUTHORS COPYING ChangeLog NEWS README THANKS
%_bindir/%name
%dir %_datadir/%name
%_datadir/%name/Images
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name.png

%files help
%_datadir/%name/Help

%files doc
%doc doc/*.pdf

%changelog
* Tue Feb 12 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.5-alt3
- NMU: fixed build with gcc-8.

* Fri Sep 05 2014 Ilya Mashkin <oddity@altlinux.ru> 4.4.5-alt2
- build for Sisyphus

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 4.4.5-alt1_11
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 4.4.5-alt1_10
- update to new release by fcimport

* Thu Mar 14 2013 Igor Vlasenko <viy@altlinux.ru> 4.4.5-alt1_9
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 4.4.5-alt1_8
- update to new release by fcimport

* Thu Dec 20 2012 Igor Vlasenko <viy@altlinux.ru> 4.4.5-alt1_7
- fc import

