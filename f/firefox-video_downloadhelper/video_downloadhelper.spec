# SPEC file for Video DownloadHelper Firefox extension

%define rname	video_downloadhelper
%define version 4.9.8
%define release alt1
%define cid	\{b9db16a4-6edc-47ec-a1f4-b86292ed211d\}
%define ciddir	%firefox_noarch_extensionsdir/%cid

Name:		%firefox_name-%rname
Version:	%version
Release:	%release

Summary:	Video DownloadHelper plugin for Firefox
Summary(ru_RU.UTF-8):	расширение Video DownloadHelper для Firefox

License:	%mpl 1.1
Group:		Networking/WWW
URL:		http://www.downloadhelper.net/
#URL:		https://addons.mozilla.org/ru/firefox/addon/3006
BuildArch:      noarch

Source0:	%rname.xpi
Packager:	Nikolay A. Fetisov <naf@altlinux.ru>

BuildRequires(pre):	rpm-build-firefox rpm-build-licenses
BuildRequires:		unzip

%description
Video DownloadHelper is a tool for web content extraction.
Its purpose is to capture video and image files from many
sites.

%description -l ru_RU.UTF-8
Расширение  Video DownloadGHelper для Firefox  предназначено
для сохранения медиа-файлов (видео- и изображений) с страниц
многих сайтов.

%prep
%setup -c

# RPM call unzip with -Lq keys, effectivly kills all mixed-case filenames in archive
rm -rf -- ./*
unzip -q %SOURCE0

%install
mkdir -p -- %buildroot/%ciddir
cp -r -- * %buildroot/%ciddir

%postun
if [ "$1" = 0 ]; then
  [ ! -d "%ciddir" ] || rm -rf "%ciddir"
fi

%files
%ciddir

%changelog
* Sun Feb 05 2012 Nikolay A. Fetisov <naf@altlinux.ru> 4.9.8-alt1
- New version

* Thu Aug 04 2011 Alexey Gladkov <legion@altlinux.ru> 4.9.4-alt1
- New version (4.9.4).

* Tue Apr 05 2011 Mykola Grechukh <gns@altlinux.ru> 4.8.6-alt1
- new version

* Wed Oct 21 2009 Nikolay A. Fetisov <naf@altlinux.ru> 4.6.4-alt1
- New version

* Thu Jun 04 2009 Alexey Gladkov <legion@altlinux.ru> 4.4.1-alt1
- New version (4.4.1)

* Sun Mar 15 2009 Nikolay A. Fetisov <naf@altlinux.ru> 4.2-alt1
- New version 

* Sun Dec 14 2008 Nikolay A. Fetisov <naf@altlinux.ru> 3.5.1-alt1
- New version 

* Fri Jul 11 2008 Nikolay A. Fetisov <naf@altlinux.ru> 3.1.1-alt1
- Initial build for ALT Linux Sisyphus
