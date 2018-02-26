Name: hnb
Version: 1.9.18
Release: alt1

Summary: Hierarchical ncurses/batch data organizer and XML editor
License: GPL
Group: Editors

Url: http://hnb.sf.net
Source0: %url/.files/%name-%version.tar.gz

Packager: Vladimir V Kamarzin <vvk@altlinux.ru>

# Automatically added by buildreq on Wed Sep 21 2005
BuildRequires: libncurses-devel libtinfo-devel

%description
hierarchical notebook (hnb) is program to organize, many kinds of data
in one place, for example adresses, todo lists, ideas, book "reviews",
brainstorming, organizing a speech, making a structured packing list
random notes, and probably many more I haven't thought of yet..

%prep
%setup -q

%build
%make

%install
%__install -pD -m0755 src/%name %buildroot%_bindir/%name
%__install -pD -m0644 doc/%name.1 %buildroot%_mandir/man1/%name.1
%__rm -f doc/%name.1

%files
%_bindir/*
%_mandir/man1/*
%doc README doc

%changelog
* Wed Sep 21 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 1.9.18-alt1
- Initial build for Sisyphus
