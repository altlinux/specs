Name: ants
Version: 0.5.3
Release: alt3
Summary: The ANTS Load Balancing System
License: %gpl2only
Group: Networking/Other
Url: http://unthought.net/antsd/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires(pre): rpm-build-licenses
BuildPreReq: gcc-c++ libncurses-devel
BuildPreReq: gkrellm-devel

Source: http://unthought.net/antsd/antsd-0.5.3.tar.gz
Patch: ants-0.5.3-alt-gcc4.3_libs.patch

%description
The ANTS Load Balancing System is a piece of software that will allow jobs to be
executed on computers connected in a network (eg. a Beowulf). The node best
suited (at the time of execution) for the job given, will be chosen to execute
the job.

This is an approach different from that of traditional Queue systems. A job is
not queued, it is executed immediately if any suitable host (for the given job
type) can be found. This makes the system suitable for execution of a large
number of small jobs, such as compilers. A traditional queue system will often
take up too much time managing it's queues, to allow tasks such as large-scale
compilations to gain much speedup using it. 

%package -n gkrellm-%name
Summary: ANTS applet for gkrellm
Group: Monitoring
Requires: %name = %version-%release
Requires: gkrellm >= 2.0

%description -n gkrellm-%name
ANTS plugin for gkrellm.

%prep
%setup
%patch -p0

%build
%configure \
	--enable-min-uid=500 \
	--disable-gnome \
	--disable-kde \
	--enable-krell \
	--enable-optimize \
	--enable-debug
%make_build

%install
%makeinstall_std

cat <<EOF >%buildroot%_sysconfdir/antsd.conf
[jobtype] [max_instances] [preferred_instances] [max_memory]
EOF
chmod 0600 %buildroot%_sysconfdir/antsd.conf

cat <<EOF >%buildroot%_sysconfdir/antsd.hosts
host1
host2
...
EOF
chmod 0600 %buildroot%_sysconfdir/antsd.hosts
cp src/antsd.hosts antsd.hosts.example
cp src/antsd.conf antsd.conf.example

%files
%doc COPYING AUTHORS src/PROTOCOL antsd.hosts.example antsd.conf.example
%_bindir/*
%_sbindir/*
%config %_sysconfdir/antsd.conf
%config %_sysconfdir/antsd.hosts

%files -n gkrellm-%name
%_libexecdir/gkrellm2/plugins/*

%changelog
* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt3
- Rebuilt for debuginfo

* Mon Oct 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt2
- Rebuilt without rpm-build-compat

* Sun Apr 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt1
- Initial build for Sisyphus

