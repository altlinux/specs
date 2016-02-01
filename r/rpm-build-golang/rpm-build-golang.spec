Name:      rpm-build-golang
Version:   1.0
Release:   alt2
Summary:   RPM helper macros to rebuild GO packages
Group:     Development/Other
License:   GPL
BuildArch: noarch
Packager:  Alexey Gladkov <legion@altlinux.ru>

Source0:   golang.macros

Source1:   golang-build
Source2:   golang-install
Source3:   golang-prepare

Source4:   golang-prov
Source5:   golang-prov.files

Source6:   golang-req
Source7:   golang-req.files

Requires:  golang

%description
These helper macros provide possibility to rebuild GO packages.

%install
mkdir -p \
	%buildroot/%_rpmlibdir \
	%buildroot/%_sysconfdir/rpm/macros.d \
	%buildroot/%_datadir/golang

cp %SOURCE0 %buildroot/%_sysconfdir/rpm/macros.d/golang
cp %SOURCE1 %SOURCE2 %SOURCE3 %buildroot/%_datadir/golang
cp %SOURCE4 %buildroot/%_rpmlibdir/golang.prov
cp %SOURCE5 %buildroot/%_rpmlibdir/golang.prov.files
cp %SOURCE6 %buildroot/%_rpmlibdir/golang.req
cp %SOURCE7 %buildroot/%_rpmlibdir/golang.req.files

%files
%_sysconfdir/rpm/macros.d/golang
%_datadir/golang
%_rpmlibdir/*

%changelog
* Mon Jan 25 2016 Alexey Gladkov <legion@altlinux.ru> 1.0-alt2
- Move go_path to _datadir/gocode.

* Tue Oct 20 2015 Alexey Gladkov <legion@altlinux.ru> 1.0-alt1
- First build.
