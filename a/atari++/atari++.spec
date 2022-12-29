# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libX11-devel libXext-devel libalsa-devel libncurses-devel
# END SourceDeps(oneline)
Name: atari++
Version: 1.85
Release: alt1
Summary: Unix based emulator of the Atari eight bit computers

Group: Emulators
License: TPL
Packager: Ilya Mashkin <oddity@altlinux.ru>
Url: http://www.xl-project.com/
Source0: http://www.xl-project.com/download/%{name}_%version.tar.gz
Source1:        http://www.xl-project.com/download/os++doc.pdf
Source2:        http://www.xl-project.com/download/basic++doc.pdf
Source3:        http://www.xl-project.com/download/system.atr
Source4:        %{name}.desktop
# borrowed from atari800 project
Source5:        atari2.svg
# be verbose during compile
Patch1: %name-verbose.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1036993
Patch2: %name-1.72-format.patch

BuildRequires: libSDL-devel libICE-devel libSM-devel zlib-devel ncurses-devel libpng-devel desktop-file-utils
Source44: import.info

%description
The Atari++ Emulator is a Unix based emulator of the Atari eight bit
computers, namely the Atari 400 and 800, the Atari 400XL, 800XL and 130XE,
and the Atari 5200 game console. The emulator is auto-configurable and
will compile on a variety of systems (Linux, Solaris, Irix).
Atari++ 1.30 and up contain a built-in ROM emulation that tries to mimic
the AtariXL operating system closely.

%prep
%setup -n %name
%patch1 -p1 -b .verbose
#patch2 -p1 -b .format

# fix encoding
f=README.History
iconv -f ISO8859-1 -t UTF-8 -o $f.new $f
touch -r $f $f.new
mv $f.new $f

# fix permissions for sources
chmod a-x *.cpp *.hpp

# additional docs
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .


%build
%configure
make %{?_smp_mflags} OPTIMIZER="$RPM_OPT_FLAGS -DDEBUG_LEVEL=0 -DCHECK_LEVEL=0" V=1

%install
make install DESTDIR=$RPM_BUILD_ROOT

# remove installed docs
rm -rf $RPM_BUILD_ROOT%_docdir/%name

# install system disk into %%_datadir
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/%{name}

# install icon
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/pixmaps

# desktop file
desktop-file-install \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications           \
        %{SOURCE4}


%files
%doc COPYRIGHT CREDITS README.LEGAL README.History README.licence manual
%doc os++doc.pdf basic++doc.pdf
%_bindir/%name
%_man6dir/%name.*
%{_datadir}/%{name}
%{_datadir}/pixmaps/atari2.svg
%{_datadir}/applications/%{name}.desktop



%changelog
* Thu Dec 29 2022 Ilya Mashkin <oddity@altlinux.ru> 1.85-alt1
- 1.85

* Sat Aug 28 2021 Ilya Mashkin <oddity@altlinux.ru> 1.84-alt1
- 1.84

* Thu Mar 18 2021 Ilya Mashkin <oddity@altlinux.ru> 1.83-alt1
- 1.83

* Mon Jul 31 2017 Ilya Mashkin <oddity@altlinux.ru> 1.81-alt1
- 1.81

* Sat Mar 29 2014 Ilya Mashkin <oddity@altlinux.ru> 1.73-alt1
- 1.73

* Wed Mar 19 2014 Ilya Mashkin <oddity@altlinux.ru> 1.72-alt2
- Build for Sisyphus

* Sat Dec 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.72-alt1_3
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.72-alt1_2
- update to new release by fcimport

* Fri Apr 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.72-alt1_1
- update to new release by fcimport

* Fri Feb 08 2013 Igor Vlasenko <viy@altlinux.ru> 1.71-alt1_1
- update to new release by fcimport

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.60-alt2_4
- update to new release by fcimport

* Tue May 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.60-alt2_3
- regenerated with 0.46 R::S::C

* Fri May 18 2012 Igor Vlasenko <viy@altlinux.ru> 1.60-alt1_3
- converted for Sisyphus

