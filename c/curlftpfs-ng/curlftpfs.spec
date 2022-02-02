Name:          curlftpfs-ng
Version:       0.9.3.1
Release:       alt0.1
Summary:       FTP filesystem, based on Curl and FUSE
Summary(ru_RU.UTF-8): Файловая система для доступа к FTP-узлам, основанная на FUSE и cURL
License:       GPL
Group:         System/Kernel and hardware
Url:           http://ikn.org.uk/tool/curlftpfs-ng/
Vcs:           https://github.com/ikn/curlftpfs-ng.git

Source:        %name-%version.tar
BuildRequires: glib2-devel
BuildRequires: libcurl-devel
BuildRequires: libfuse-devel

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


%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall
mkdir %buildroot/sbin
ln -s /usr/bin/curlftpfs  %buildroot/sbin/mount.curlftpfs

%files
/sbin/mount.curlftpfs
%_bindir/curlftpfs
%_man1dir/curlftpfs.1.*


%changelog
* Wed Feb 02 2022 Pavel Skrylev <majioa@altlinux.org> 0.9.3.1-alt0.1
- Initial build v0.9.3[.1] for Sisyphus
