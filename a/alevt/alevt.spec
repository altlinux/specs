Name: alevt
Version: 1.6.2
Release: alt2_16
Summary: Teletext decoder/browser
Group: Video
License: GPLv2
URL: http://goron.de/~froese
Source: http://goron.de/~froese/%{name}/%{name}-%{version}.tar.gz
Source1: alevt.desktop
Patch0: alevt-1.6.2-pixmap.patch
Patch1: alevt-1.6.2-manpath.patch
Patch2: alevt-1.6.2-rus-greek.patch
Patch3: alevt-1.6.2-doublefont.patch
BuildRequires: libX11-devel
BuildRequires: libpng-devel
BuildRequires: desktop-file-utils
BuildRequires: ImageMagick
Source44: import.info

%description
AleVT is a teletext/videotext decoder and browser for the
vbi (/dev/vbi) device and X11.  It features multiple windows,
a page cache, regexp searching, built-in manual, and more.
There's also a program to get the time from teletext and
one to capture teletext pages from scripts.


%prep
%setup -q
%patch0 -p1 -b .pixmap
%patch1 -p1 -b .manpath
%patch2 -p1 -b .rusgreek
%patch3 -p1 -b .double

%build
# alevt does not have standard build system, so we populate OPT, 
# which is internal build variable to accommodate Fedora opt flags
# This will produce lot of garbage on output.
make %{?_smp_mflags} -e OPT="%{optflags}"


%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1

make USR_X11R6=%{_prefix} MAN=%{_mandir} rpm-install
desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications %{SOURCE1}


%files
%{_bindir}/alevt
%{_bindir}/alevt-date
%{_bindir}/alevt-cap
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man?/%{name}*
%{_datadir}/pixmaps/mini-alevt.xpm
%doc README CHANGELOG COPYRIGHT

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt2_16
- rebuild to get rid of #27020

* Fri Jul 08 2011 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_16
- initial release by fcimport

