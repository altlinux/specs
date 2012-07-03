# SPEC file for olive
#

%define real_name    olive
%define version      1.3
%define real_version 1.3
%define release      alt1

Name:     %real_name
Version:  %version
Release:  %release

Summary: Olive is a console mode RSS aggregator / newsreader
Summary(ru_RU.UTF-8): Olive - утилита получения и просмотра новостей RSS

Group:    Networking/News
License:  Perl license
URL:      http://firepear.net/olive/

Packager: Nikolay Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source0: http://mdxi.collapsar.net/hacks/olive/releases/%real_name-%real_version.tar.bz2
Source1: OliveLog-2.110.tar.bz2
Patch0: olive-b12-alt-log_dispatch.patch
Patch1: olive-b12-alt-browser_config.patch

AutoReqProv: perl, yes
BuildPreReq: perl-devel, perl-Config-YAML, perl-Curses-UI, perl-Date-Calc
BuildPreReq: perl-DBD-SQLite, perl-XML-Parser, perl-XML-Simple, perl-Encode
BuildPreReq: perl-libwww, perl-DBI, perl-Params-Validate

# For some reason perl-XML-SAX doesn't work with perl-XML-Simple
# And DBD::SQLite is missed from view of find-requires
Requires:    perl-DBD-SQLite perl-XML-Parser


%description
Olive is a totally sweet console mode RSS aggregator / newsreader
written in Perl with Curses::UI as its toolkit.
 
The big difference between Olive and other newsreaders is that it
takes a time-centric as opposed to site-centric view of newsfeeds.

Olive shows  news stories  from all feeds at once,  arranged them
from the oldest unread story to newest one, and then  from newest 
previously read to the oldest one.


%description -l ru_RU.UTF-8
Olive - привлекательная утилита для получения и просмотра новостей
каналов  RSS для консоли,  написанная на  Perl  и использующая для 
интерфейса с пользователем Curses::UI. 

Основное отличие Olive от других программ просмотра новостей в том,
что она  ориентирована на сортировку новостей  по времени,  а не по 
источнику.   Olive  упорядочивает  список новостей от  самой старой 
непросмотренной к самой новой, и далее от самой новой просмотренной
в предыдущем сеансе к самой старой.

%define libdir %_datadir/%real_name

%define _perl_lib_path %libdir

%prep
%setup -q -n %real_name-%real_version
%patch0
%patch1
subst 's/Log::Dispatch/OliveLog::Dispatch/' OliveMisc.pm
tar xvfj %SOURCE1

%build
%make

%install
mkdir -p -- $RPM_BUILD_ROOT%libdir
%make install DESTDIR=$RPM_BUILD_ROOT PREFIX=%_prefix DOCDIR=%_docdir/%real_name-%version/docs
mkdir -p -- $RPM_BUILD_ROOT%libdir/OliveLog/Dispatch
install -m 0644 -- OliveLog/Dispatch.pm        $RPM_BUILD_ROOT%libdir/OliveLog/Dispatch.pm 
install -m 0644 -- OliveLog/Dispatch/Base.pm   $RPM_BUILD_ROOT%libdir/OliveLog/Dispatch/Base.pm
install -m 0644 -- OliveLog/Dispatch/File.pm   $RPM_BUILD_ROOT%libdir/OliveLog/Dispatch/File.pm
install -m 0644 -- OliveLog/Dispatch/Output.pm $RPM_BUILD_ROOT%libdir/OliveLog/Dispatch/Output.pm

%files
%doc README CHANGELOG
%doc docs*
     %_bindir/%real_name
%dir %libdir/
%dir %libdir/OliveLog/
%dir %libdir/OliveLog/Dispatch/
     %libdir/Olive*.pm
     %libdir/OliveLog/Dispatch.pm
     %libdir/OliveLog/Dispatch/*.pm

%changelog
* Thu Aug 9 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.3-alt1
- New version 1.3
  * Fixes a typo in the previous release which led to a crashing bug
  * Versioning change for Debian packaging.
- URL updated

* Mon May 07 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.3-alt1
- New version r1 patch level 3
  * bugfix for 'Add New Feed' dialog
  * Update URLs in help panel

* Tue Mar 27 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.2-alt1
- New version r1 patch level 2
  * "Keep stories until read" option added
  * URL in help panel fixed
- spec file cleanup

* Sun Feb 19 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.1-alt1
- New version r1 patch level 1
  * Fix for story selection problem after (un)starring a story
  * Fix license information in files
  * -h/--help and -v/--verbose options added

* Sat Feb 04 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.0-alt1
- New version r1
  * Several bug fixes
  * Release version R1

* Sun Jan 29 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.13-alt1
- New version b13
- Removing several patches applied by mainstream
- Adding Log::Dispatch::File module to Ovile distribution to avoid
  dependences overhead from perl-Log-Dispatch package

* Mon Jan 09 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.11-alt1
- Initial build for ALTLinux Sisyphus

