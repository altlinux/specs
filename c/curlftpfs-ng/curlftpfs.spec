%define        _unpackaged_files_terminate_build 1
%define        nomen curlftpfs
%def_enable    devel
%def_disable   check

Name:          %nomen-ng
Version:       0.9.3.11
Release:       alt0.1
Summary:       FTP filesystem, based on Curl and FUSE
Summary(ru_RU.UTF-8): Файловая система для доступа к FTP-узлам, основанная на FUSE и cURL
License:       GPLv2
Group:         System/Kernel and hardware
Url:           http://ikn.org.uk/tool/curlftpfs-ng/
Vcs:           https://github.com/malbajun/curlftpfs-ng.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-cmake
BuildRequires: /proc
%{?_enable_check:BuildRequires: ctest}
BuildRequires: glib2-devel
BuildRequires: libcurl-devel
BuildRequires: pkgconfig(fuse3)
BuildRequires: pkgconfig(libpcre2-8)

Conflicts:     curlftpfs

%description
CurlFtpFS is a filesystem for accessing FTP hosts based on FUSE and
libcurl. CurlFtpFS differentiates itself from other FTP filesystems
because it features:
- SSLv3 and TLSv1 support
- connecting through tunneling HTTP proxies
- automatically reconnection if the server times out
- transform absolute symlinks to point back into the ftp file system

%description -l ru_RU.UTF-8
CurlFtpFS — это инструмент для подключения узлов FTP как локальных
директорий. Он соединяется с FTP-сервером и отображает структуру его
директорий в локальной файловой системе.

CurlFtpFS основан на FUSE (filesystem in userspace — файловая система в
пользовательском пространстве) и библиотеке cURL и имеет некоторые
особенности, которые отличают его от других файловых систем FTP:
- поддержка соединения по SSLv3 и TLSv1;
- соединение через туннелирующие HTTP-прокси;
- автоматическое переподключение при разрыве соединения;
- абсолютные символьные ссылки преобразуются и указывают на файловую
  систему FTP.


%package       -n lib%{nomen}
Summary:       FTP filesystem, based on Curl and FUSE library
Summary(ru_RU.UTF-8): Библиотека файловой системы для доступа к FTP-узлам, основанной на FUSE и cURL
Group:         System/Libraries

%description   -n lib%{nomen}
FTP filesystem, based on Curl and FUSE library.

CurlFtpFS is a filesystem for accessing FTP hosts based on FUSE and
libcurl. CurlFtpFS differentiates itself from other FTP filesystems
because it features:
- SSLv3 and TLSv1 support
- connecting through tunneling HTTP proxies
- automatically reconnection if the server times out
- transform absolute symlinks to point back into the ftp file system

%description   -n lib%{nomen} -l ru_RU.UTF-8
Библиотека файловой системы для доступа к FTP-узлам, основанной на FUSE и cURL.

CurlFtpFS — это инструмент для подключения узлов FTP как локальных
директорий. Он соединяется с FTP-сервером и отображает структуру его
директорий в локальной файловой системе.

CurlFtpFS основан на FUSE (filesystem in userspace — файловая система в
пользовательском пространстве) и библиотеке cURL и имеет некоторые
особенности, которые отличают его от других файловых систем FTP:
- поддержка соединения по SSLv3 и TLSv1;
- соединение через туннелирующие HTTP-прокси;
- автоматическое переподключение при разрыве соединения;
- абсолютные символьные ссылки преобразуются и указывают на файловую
  систему FTP.


%if_enabled    devel
%package       -n lib%{nomen}-devel
Summary:       FTP filesystem, based on Curl and FUSE development package
Summary(ru_RU.UTF-8): Файлы разработки файловой системы для доступа к FTP-узлам, основанной на FUSE и cURL
Group:         Development/C

%{?_enable_check:Requires: ctest}
Requires:      glib2-devel
Requires:      libcurl-devel
Requires:      pkgconfig(fuse3)
Requires:      pkgconfig(libpcre2-8)

%description   -n lib%{nomen}-devel
FTP filesystem, based on Curl and FUSE development package.

CurlFtpFS is a filesystem for accessing FTP hosts based on FUSE and
libcurl. CurlFtpFS differentiates itself from other FTP filesystems
because it features:
- SSLv3 and TLSv1 support
- connecting through tunneling HTTP proxies
- automatically reconnection if the server times out
- transform absolute symlinks to point back into the ftp file system

%description   -n lib%{nomen}-devel -l ru_RU.UTF-8
Файлы разработки файловой системы для доступа к FTP-узлам, основанной на FUSE и cURL

CurlFtpFS — это инструмент для подключения узлов FTP как локальных
директорий. Он соединяется с FTP-сервером и отображает структуру его
директорий в локальной файловой системе.

CurlFtpFS основан на FUSE (filesystem in userspace — файловая система в
пользовательском пространстве) и библиотеке cURL и имеет некоторые
особенности, которые отличают его от других файловых систем FTP:
- поддержка соединения по SSLv3 и TLSv1;
- соединение через туннелирующие HTTP-прокси;
- автоматическое переподключение при разрыве соединения;
- абсолютные символьные ссылки преобразуются и указывают на файловую
  систему FTP.
%endif


%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%check
%ctest

%files
%_sbindir/mount.%{nomen}
%_sbindir/%{nomen}
%_mandir/%{nomen}.1.*

%files         -n lib%{nomen}
%_libdir/lib%{nomen}*.so.*

%if_enabled    devel
%files         -n lib%{nomen}-devel
%doc README COPYING ChangeLog release
%_cmakedir/%nomen/%{nomen}*.cmake
%_libdir/lib%{nomen}*.so
%endif


%changelog
* Mon Aug 03 2026 Pavel Skrylev <majioa@altlinux.org> 0.9.3.11-alt0.1
- 0.9.3[.1] -> 0.9.3p11
- * turned from configure to cmake
- ^ bumped to fuse3
- !FTBFS fixed

* Wed Feb 02 2022 Pavel Skrylev <majioa@altlinux.org> 0.9.3.1-alt0.1
- Initial build v0.9.3[.1] for Sisyphus
