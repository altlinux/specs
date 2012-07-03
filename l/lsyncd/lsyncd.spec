Name: lsyncd
Version: 2.0.5
Release: alt1
Summary: File change monitoring and synchronization daemon

Group: File tools
License: %gpl2plus
Url: http://code.google.com/p/lsyncd/
Source0: http://lsyncd.googlecode.com/files/%name-%version.tar.gz

BuildRequires: liblua5-devel rpm-build-licenses lua5

%description
Lsyncd watches a local directory trees event monitor interface (inotify).
It aggregates and combines events for a few seconds and then spawns one
(or more) process(es) to synchronize the changes. By default this is
rsync.

Lsyncd is thus a light-weight live mirror solution that is comparatively
easy to install not requiring new file systems or block devices and does
not hamper local file system performance.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_man1dir/%name.1*
%doc ChangeLog examples

%changelog
* Sat Jan  7 2012 Terechkov Evgenii <evg@altlinux.org> 2.0.5-alt1
- Initial build for ALT Linux Sisyphus
