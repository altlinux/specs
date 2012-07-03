Name: simh
Version: 3.8.1
Release: alt0.6
Summary: A highly portable, multi-system emulator

Group: Emulators
#The licensing is mostly MIT, but there is also some GPL+ (literally, v1+) code
#in there, notably in AltairZ80/.
#(each target is compiled into its own binary, so only AltairZ80 is GPL+)
License: MIT and GPL+

Url: http://simh.trailing-edge.com/
Packager: Andrey Bergman <vkni@altlinux.org>

Source: %name-%version.tar

# prefer default gnu89 (ISO C90) as C99 is not fully supported by cc
# and add fedora optflags
Patch: simh-3.8.0-gcc.patch
Patch1: simh-3.8.1-altair-segfault.patch
Patch2: simh-alt-ldflags.patch

BuildRequires: libpcap-devel recode

%description
SIMH is a historical computer simulation system. It consists of simulators
for many different computers, all written around a common user
interface package and set of supporting libraries.
SIMH can be used to simulate any computer system for which sufficient detail
is available, but the focus to date has been on simulating computer systems
of historic interest.

SIMH implements simulators for:

* Data General Nova, Eclipse
* Digital Equipment Corporation PDP-1, PDP-4, PDP-7, PDP-8, PDP-9,
  PDP-10, PDP-11, PDP-15, VAX
* GRI Corporation GRI-909, GRI-99
* IBM 1401, 1620, 7090/7094, System 3
* Interdata (Perkin-Elmer) 16b and 32b systems
* Hewlett-Packard 2114, 2115, 2116, 2100, 21MX, 1000
* Honeywell H316/H516
* MITS Altair 8800, with both 8080 and Z80
* Royal-Mcbee LGP-30, LGP-21
* Scientific Data Systems SDS 940

%description -l ru_RU.UTF-8
SIMH - это система эмуляторов, моделирующих устаревшие и давно снятые
с производства компьютеры. Эмуляторы simh имеют один и тот же интерфейс
и базируются на общих библиотеках. И хотя на основе системы simh можно
построить эмулятор любой ЭВМ, в данный момент основным приложением
являются системы, имеющие исторический интерес.

В пакет входят эмуляторы для:

* Data General Nova, Eclipse
* Digital Equipment Corporation PDP-1, PDP-4, PDP-7, PDP-8, PDP-9,
  PDP-10, PDP-11, PDP-15, VAX
* GRI Corporation GRI-909, GRI-99
* IBM 1401, 1620, 7090/7094, System 3
* Interdata (Perkin-Elmer) 16b and 32b systems
* Hewlett-Packard 2114, 2115, 2116, 2100, 21MX, 1000
* Honeywell H316/H516
* MITS Altair 8800, with both 8080 and Z80
* Royal-Mcbee LGP-30, LGP-21
* Scientific Data Systems SDS 940

Образы операционных систем для этих компьютеров можно, например,
скачать с домашней страницы simh или страницы русских любителей PDP
http://pdp-11.org.ru

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
mkdir -p BIN
%make_build -e OPT="%optflags" USE_NETWORK=1

%install
mkdir -p %buildroot%_bindir
for i in `ls BIN/`; do
	install -p -m 755 BIN/$i %buildroot%_bindir/simh-$i
done
mkdir -p %buildroot%_docdir/%name-%version
for i in `find -iname "*.txt"`; do recode cp1251/CR-LF.. $i; done

%files
%_bindir/*
%doc ALTAIR/altair.txt NOVA/eclipse.txt 0readme_38.txt 0readme_ethernet.txt
%doc HP2100/hp2100_diag.txt I7094/i7094_bug_history.txt Interdata/id_diag.txt
%doc PDP1/pdp1_diag.txt PDP10/pdp10_bug_history.txt PDP18B/pdp18b_diag.txt
%doc S3/haltguide.txt S3/readme_s3.txt S3/system3.txt SDS/sds_diag.txt
%doc VAX/vax780_bug_history.txt
%doc DOC/*.pdf

%changelog
* Tue Dec 07 2010 Andrey Bergman <vkni@altlinux.org> 3.8.1-alt0.6
- Added detailed documentation.

* Mon Dec 06 2010 Andrey Bergman <vkni@altlinux.org> 3.8.1-alt0.5
- Added russian description.

* Wed Dec 01 2010 Andrey Bergman <vkni@altlinux.org> 3.8.1-alt0.4
- Added proper build requires. 

* Wed Dec 01 2010 Andrey Bergman <vkni@altlinux.org> 3.8.1-alt0.3
- Group changed to Emulators.

* Wed Dec 01 2010 Andrey Bergman <vkni@altlinux.org> 3.8.1-alt0.2
- Removed generate tarball script.

* Wed Dec 01 2010 Andrey Bergman <vkni@altlinux.org> 3.8.1-alt0.1
- initial build for ALT Linux Sisyphus (spec copied from Fedora)
