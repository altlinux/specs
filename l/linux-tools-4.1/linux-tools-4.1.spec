%define kernel_base_version 4.1
%define kernel_source kernel-source-%kernel_base_version
%add_verify_elf_skiplist %_libexecdir/traceevent_%kernel_base_version/plugins/*
%add_findreq_skiplist %_datadir/perf_%kernel_base_version-core/tests/*.py
%set_compress_method gzip

Name: linux-tools-%kernel_base_version
Version: %kernel_base_version
Release: alt1.1.1.1

Summary: Performance analysis tools for Linux
License: GPLv2
Group: Development/Tools
URL: http://www.kernel.org/

BuildRequires: libaudit-devel elfutils-devel libnuma-devel perl-devel libslang2-devel libunwind-devel bison flex binutils-devel asciidoc xmlto
BuildRequires: rpm-build-kernel
BuildRequires: %kernel_source = 1.0.0

Patch1: linux-tools-4.1-alt.patch

AutoReq: yes,noperl,nopython
AutoProv: yes,noperl,nopython

%description
Performance counters for Linux are a new kernel-based subsystem that provide
a framework for all things performance analysis. It covers hardware level
(CPU/PMU, Performance Monitoring Unit) features and software features
(software counters, tracepoints) as well.
This package contains performance analysis tools for Linux

%prep
%setup -cT
tar -xf %kernel_src/%kernel_source.tar*
cd %kernel_source
%patch1 -p1

%build
%install
pushd %kernel_source/tools/perf
sed -i 's|\(perfexecdir[[:blank:]]*=[[:blank:]]*\).*$|\1share/perf_%kernel_base_version-core|' config/Makefile
sed -i 's|\(plugindir[[:blank:]]*=[[:blank:]]*\).*$|\1%_libexecdir/traceevent_%kernel_base_version/plugins|' config/Makefile
make VERSION=%kernel_base_version \
     V=1 \
     VF=1 \
     WERROR=0 \
     NO_GTK2=1 \
     DESTDIR=%buildroot \
     prefix=%_prefix \
     all \
     man \
     install \
     install-man

install -d -m 0755 %buildroot%_docdir/%name
install -m 0644 {CREDITS,design.txt,Documentation/examples.txt} %buildroot%_docdir/%name/
popd

# Make alternatives:
mkdir -p %buildroot%_altdir
cat <<'_EOF'_ > %buildroot%_altdir/%name.alternatives
%_bindir/perf	%_bindir/perf_%kernel_base_version	10
%_bindir/perf	%_bindir/perf_%kernel_base_version	10
%_bindir/trace	%_bindir/trace_%kernel_base_version	10
%_sysconfdir/bash_completion.d/perf	%_sysconfdir/bash_completion.d/perf_%kernel_base_version	10
_EOF_

# Add man alternatives:
pushd %buildroot%_man1dir
for file in *.1;do
alterfile=`echo $file|sed -e "s|_%kernel_base_version||"`
echo "%_man1dir/$alterfile.gz	%_man1dir/$file.gz	10" >> %buildroot%_altdir/%name.alternatives
done
popd

%files
%_altdir/%name.alternatives
%_bindir/perf_%kernel_base_version
%_bindir/trace_%kernel_base_version
%_man1dir/*.1.gz
%_sysconfdir/bash_completion.d/perf_%kernel_base_version
%_libexecdir/traceevent_%kernel_base_version
%_datadir/perf_%kernel_base_version-core
%doc %_docdir/%name

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1.1
- rebuild with new perl 5.22.0

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
