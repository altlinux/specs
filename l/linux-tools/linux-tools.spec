%define kernel_base_version 4.12
%define kernel_source kernel-source-%kernel_base_version
%add_verify_elf_skiplist %_libexecdir/traceevent_%kernel_base_version/plugins/*
%add_findreq_skiplist %_datadir/perf_%kernel_base_version-core/tests/*.py
%set_compress_method gzip

Name: linux-tools
Version: %kernel_base_version
Release: alt2.1

Summary: Performance analysis tools for Linux
License: GPLv2
Group: Development/Tools
URL: http://www.kernel.org/

BuildRequires: libaudit-devel elfutils-devel libnuma-devel perl-devel libslang2-devel libunwind-devel bison flex binutils-devel asciidoc xmlto libssl-devel liblzma-devel
BuildRequires: rpm-build-kernel
BuildRequires: %kernel_source = 1.0.0
BuildRequires: python-devel

# Broken in upstream, waiting for fix...
ExclusiveArch: x86_64

Patch1: linux-tools-alt.patch
Patch2: python-linking.patch

AutoReq: yes,noperl,nopython
AutoProv: yes,noperl,nopython

%package -n python-module-perf
Summary: Python bindings for apps which will manipulate perf events
Group: Development/Python
Provides: python-perf

%description
Performance counters for Linux are a new kernel-based subsystem that provide
a framework for all things performance analysis. It covers hardware level
(CPU/PMU, Performance Monitoring Unit) features and software features
(software counters, tracepoints) as well.
This package contains performance analysis tools for Linux

%description -n python-module-perf
The python-perf package contains a module that permits applications
written in the Python programming language to use the interface
to manipulate perf events.

%prep
%setup -cT
tar -xf %kernel_src/%kernel_source.tar*
cd %kernel_source
%patch1 -p1
%patch2 -p1

%build
%install
pushd %kernel_source/tools/perf
sed -i 's|\(perfexecdir[[:blank:]]*=[[:blank:]]*\).*$|\1share/perf_%kernel_base_version-core|' Makefile.config
sed -i 's|\(plugindir[[:blank:]]*=[[:blank:]]*\).*$|\1%_libexecdir/traceevent_%kernel_base_version/plugins|' Makefile.config
sed -i 's|\(STRACE_GROUPS_DIR[[:blank:]]*=[[:blank:]]*\).*$|\1share/perf_%kernel_base_version-core/strace/groups|' Makefile.config
make VERSION=%kernel_base_version \
     VF=1 \
     WERROR=0 \
     NO_GTK2=1 \
     PYTHON=python2 \
     PYTHON_CONFIG=python2-config \
     DESTDIR=%buildroot \
     prefix=%_prefix \
     install \
     install-man \
     install-python_ext

install -d -m 0755 %buildroot%_docdir/%name
install -m 0644 {CREDITS,design.txt,Documentation/examples.txt,Documentation/tips.txt} %buildroot%_docdir/%name/
popd

# Make alternatives:
mkdir -p %buildroot%_altdir
cat <<'_EOF'_ > %buildroot%_altdir/%name
%_bindir/perf	%_bindir/perf_%kernel_base_version	20
%_bindir/trace	%_bindir/trace_%kernel_base_version	20
%_sysconfdir/bash_completion.d/perf	%_sysconfdir/bash_completion.d/perf_%kernel_base_version	20
_EOF_

# Add man alternatives:
pushd %buildroot%_man1dir
for file in *.1;do
alterfile=`echo $file|sed -e "s|_%kernel_base_version||"`
echo "%_man1dir/$alterfile.gz	%_man1dir/$file.gz	20" >> %buildroot%_altdir/%name
done
popd

%files
%_altdir/%name
%_bindir/perf_%kernel_base_version
%_bindir/trace_%kernel_base_version
%_man1dir/*.1.gz
%_sysconfdir/bash_completion.d/perf_%kernel_base_version
%_libexecdir/traceevent_%kernel_base_version
%_datadir/perf_%kernel_base_version-core
%doc %_docdir/%name

%files -n python-module-perf
%python_sitelibdir/perf*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 4.12-alt2.1
- rebuild with new perl 5.26.1

* Wed Aug  2 2017 Terechkov Evgenii <evg@altlinux.org> 4.12-alt2
- Build exclusively for x86_64 for now, waiting for upstream fix...

* Thu Jul 13 2017 Terechkov Evgenii <evg@altlinux.org> 4.12-alt1
- Update for kernel-4.12

* Wed Mar 29 2017 Terechkov Evgenii <evg@altlinux.org> 4.10-alt1
- Update for kernel-4.10
- Fix minor repocop warning about python-dev

* Wed Feb  8 2017 Terechkov Evgenii <evg@altlinux.org> 4.9-alt4
- Add python-module-perf subpackage

* Wed Feb  8 2017 Terechkov Evgenii <evg@altlinux.org> 4.9-alt3
- Add patch2 to linking python

* Wed Feb  8 2017 Terechkov Evgenii <evg@altlinux.org> 4.9-alt2
- Build with python support

* Mon Feb 06 2017 Igor Vlasenko <viy@altlinux.ru> 4.9-alt1.1
- rebuild with new perl 5.24.1

* Fri Feb  3 2017 Terechkov Evgenii <evg@altlinux.org> 4.9-alt1
- Update for kernel-4.9

* Wed Oct 19 2016 Terechkov Evgenii <evg@altlinux.org> 4.7-alt1
- Clone package from linux-tools-4.4
- TODO: build with python support

* Thu Jan 28 2016 Terechkov Evgenii <evg@altlinux.org> 4.4-alt1
- Clone package from linux-tools-4.3

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1.1
- rebuild with new perl 5.22.0

* Wed Nov  4 2015 Terechkov Evgenii <evg@altlinux.org> 4.3-alt1
- Clone package from linux-tools-4.2

* Sat Oct 10 2015 Terechkov Evgenii <evg@altlinux.org> 4.2-alt1
- Clone package from linux-tools-4.1

* Fri Oct  2 2015 Terechkov Evgenii <evg@altlinux.org> 4.1-alt1
- Clone package from linux-tools-4.0

* Mon Jul 13 2015 Terechkov Evgenii <evg@altlinux.org> 4.0-alt2
- Return bin/trace (hardlink to bin/perf) for convience
- Additional alternatives (man1dir/bash_completion/trace)

* Sun Jul 12 2015 Terechkov Evgenii <evg@altlinux.org> 4.0-alt1
- Clone package from linux-tools-3.14
- Rediffed patches

* Sun Jul 12 2015 Terechkov Evgenii <evg@altlinux.org> 3.14-alt4
- Add tools-perf-install.patch from Debian

* Sun Jul 12 2015 Terechkov Evgenii <evg@altlinux.org> 3.14-alt3
- Add basic alternatives support
- Make different kernel versions non-conflicting

* Sun Jul 12 2015 Terechkov Evgenii <evg@altlinux.org> 3.14-alt2
- Add tool-perf-version.patch from Debian

* Sat Jul 11 2015 Terechkov Evgenii <evg@altlinux.org> 3.14-alt1
- Initial build for ALT Linux
