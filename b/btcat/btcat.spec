Name: btcat
Version: 0.1
Release: alt1

Summary: Btcat is a torrent command line tool
License: %gpl3plus
Group: Networking/WWW
Url: http://jordic.com/btcat

Patch0: btcat-0.1-drop-unnecessary-Tkinter-dependence.patch
BuildArch: noarch

Source: btcat

BuildPreReq: rpm-build-licenses
BuildRequires: python-devel

%description
btcat is a command line tool that downloads a file using the bittorrent
protocol and outputs its contents to the standard output. btcat streams
the data sequentially, which allows processing the file in a pipeline
before the whole transfer has been completed. It is possible, for
instance, to reproduce a media file while it's still downloading.

%prep
%setup -c -T -n %name-%version
cp %_sourcedir/btcat .
%patch0 -p1

%install
mkdir -p %buildroot/%_bindir
cp btcat %buildroot/%_bindir/

%files
%_bindir/btcat

%changelog
* Fri Feb 01 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1-alt1
- Initial build
