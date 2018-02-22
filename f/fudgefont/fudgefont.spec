# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name fudgefont
%define major   1
%define libname lib%{name}%{major}
%define devname lib%{name}-devel

Name:           fudgefont
Version:        1.4
Release:        alt1_3
Summary:        Fudges TTF fonts into Allegro
Group:          System/Libraries
# The license was specified on the website back in 2008:
# https://web.archive.org/web/20080417111542/http://fudgefont.sourceforge.net/
License:        MIT
URL:            http://fudgefont.sourceforge.net/
Source0:        http://downloads.sf.net/fudgefont/%{name}-%{version}-src.7z

BuildRequires:  liballegro-devel
BuildRequires:  p7zip p7zip-standalone
BuildRequires:  pkgconfig(freetype2)
Source44: import.info

%description
FudgeFont is an addon for Allegro 4 which allows reading .ttf files
(by using libfreetype) and use them with Allegro's normal font routines.
This works by internally converting the TTF font into a bitmap font.
It has full unicode.

#----------------------------------------------------------------------

%package -n %{libname}
Summary:        Fudges TTF fonts into Allegro
Group:          System/Libraries

%description -n %{libname}
FudgeFont is an addon for Allegro 4 which allows reading .ttf files
(by using libfreetype) and use them with Allegro's normal font routines.
This works by internally converting the TTF font into a bitmap font.
It has full unicode.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

#----------------------------------------------------------------------

%package -n %{devname}
Summary:        Development files for the FudgeFont Allegro 4 addon
Group:          Development/C++
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel

%description -n %{devname}
This package contains a development header and library for the FudgeFont
Allegro 4 addon.

%files -n %{devname}
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

#----------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}-src -c -T
cd ..
7z x %SOURCE0

%build
# Bypassing the scons BS to add the missing soname
CFLAGS="%{optflags} -fPIC `freetype-config --cflags`"
LIBS="`freetype-config --libs` `allegro-config --libs`"

gcc ${CFLAGS} -o fudgefont.os -c -fPIC src/fudgefont.c
gcc ${CFLAGS} -o kerning.os -c -fPIC src/kerning.c
gcc ${CFLAGS}  -Wl,-soname,lib%{name}.so.%{major} -o lib%{name}.so.%{version} \
    -shared fudgefont.os kerning.os ${LIBS}

ln -s lib%{name}.so.%{version} lib%{name}.so.%{major}
ln -s lib%{name}.so.%{major} lib%{name}.so

%install
install -D -m644 src/%{name}.h %{buildroot}%{_includedir}/%{name}.h

install -d %{buildroot}%{_libdir}
cp -pP lib%{name}.so* %{buildroot}%{_libdir}


%changelog
* Tue Feb 20 2018 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_3
- update by mgaimport

* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_2
- converted for ALT Linux by srpmconvert tools

