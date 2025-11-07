%define        _unpackaged_files_terminate_build 1

Name:          ttf2pt1
Version:       3.4.5.2
Release:       alt1
Group:         Publishing
Summary:       True Type Font to Postscript Type 1 Converter
License:       GPLv2+ and BSD with advertising
Url:           https://ttf2pt1.sourceforge.net/
Vcs:           https://github.com/william8000/ttf2pt1.git

Source:        %name-%version.tar
BuildRequires: libfreetype-devel
BuildRequires: t1lib-devel
BuildRequires: perl-podlators

Requires:      t1utils

%description
Ttf2pt1 is a font converter from the True Type format (and some other formats
supported by the FreeType library as well) to the Adobe Type1 format.

%prep
%setup -q

%build
%make all -C ttf2pt1

%install
%make install -C ttf2pt1 DESTDIR=%buildroot INSTDIR=%prefix MANDIR=%_mandir LIBXDIR=%_libexecdir/%name


%files
%doc %name/CHANGES* %name/README* %name/FONTS*
%_bindir/%{name}*
%_man1dir/%{name}*.1*
%_datadir/%name/
%_libexecdir/%name/


%changelog
* Fri Nov 07 2025 Pavel Skrylev <majioa@altlinux.org> 3.4.5.2-alt1
- ^ 3.4.4 -> 3.4.5.2

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.4.4-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Aug 17 2009 Michael A. Kangin <prividen@altlinux.org> 3.4.4-alt1
- Initial build for Sisyphus
