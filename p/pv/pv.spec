# Spec file for pv - Pipe Viewer 

Name: pv
Version: 1.1.4
Release: alt1

Summary: Pipe Viewer

#%%gpl2plus 
License: %artistic_license
Group: Text tools
URL: http://www.ivarch.com/programs/pv.shtml

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: http://pipeviewer.googlecode.com/files/%name-%version.tar.bz2

BuildRequires(pre): rpm-build-licenses

%description
pv - Pipe Viewer - is a terminal-based tool for monitoring the
progress of data through a pipeline. It can be inserted into
any normal pipeline between two processes to give a visual
indication of how quickly data is passing through, how long it
has taken, how near to completion it is, and an estimate of
how long it will be until completion.

Additional support is available for multiple instances working
in tandem, to given a visual indicator of relative throughput
in a complex pipeline.

%prep
%setup -q

pushd doc
mv -f -- COPYING COPYING.orig
ln -s -- $(relative %_licensedir/Artistic-2 %_docdir/%name/COPYING) COPYING
popd

%build
pushd autoconf/
autoconf configure.in > ../configure
popd
touch autoconf/make/{depend.mk~,filelist.mk~,modules.mk~}
chmod u+x configure

%configure
make make
make dep
%make_build

%install
%make_install DESTDIR=%buildroot install
%find_lang %name

%files -f %name.lang
%doc doc/NEWS doc/TODO 
%doc --no-dereference doc/COPYING

%_bindir/%name
%_man1dir/%name.*

%changelog
* Mon May 19 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.1.4-alt1
- Initial build for ALT Linux Sisyphus
