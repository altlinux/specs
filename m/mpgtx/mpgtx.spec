Name: mpgtx
Version: 1.3.1
Release: alt1

Summary: MPeG ToolboX
License: GPL
Group: Video
URL: http://mpgtx.sourceforge.net/

Source: http://dl.sourceforge.net/mpgtx/mpgtx-%version.tar.gz

# Automatically added by buildreq on Tue Feb 22 2005
BuildRequires: gcc-c++ libstdc++-devel

%description
mpgtx allows you to split, join, demultiplex, manipulate ID3 tags and
fetch detailed information about a variety of MPEG files.

%prep
%setup -q

%build
./configure --prefix=/usr
%make_build

%install
%__make install \
	PREFIX=$RPM_BUILD_ROOT/usr manprefix=$RPM_BUILD_ROOT/usr/share
rm -rf $RPM_BUILD_ROOT%_mandir/de

%files
%doc AUTHORS ChangeLog README TODO
%_bindir/*
%_man1dir/*

%changelog
* Fri Feb 25 2005 Victor Forsyuk <force@altlinux.ru> 1.3.1-alt1
- Initial build for Sisyphus.
