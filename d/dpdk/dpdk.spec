# Add option to build as static libraries (--without shared)
%def_with shared
# Add option to build without examples
%def_with examples
# Add option to build without tools
%def_with tools
# Add option to build the PDF documentation separately (--with pdfdoc)
%def_without pdfdoc

%def_without doc

Name: dpdk
Version: 16.11
Release: alt1
Url: http://dpdk.org
Packager: Lenar Shakirov <snejok@altlinux.ru>

Source: %name-%version.tar

Patch0: %name-%version-move-to-libdir.patch

Summary: Set of libraries and drivers for fast packet processing
Group: System/Libraries

#
# Note that, while this is dual licensed, all code that is included with this
# Pakcage are BSD licensed. The only files that aren't licensed via BSD is the
# kni kernel module which is dual LGPLv2/BSD, and thats not built for fedora.
#
License: BSD and LGPLv2 and GPLv2

#
# The DPDK is designed to optimize througput of network traffic using, among
# other techniques, carefully crafted x86 assembly instructions.  As such it
# currently (and likely never will) run on non-x86 platforms
#
ExclusiveArch: x86_64 i586

# machine_arch maps between rpm and dpdk arch name, often same as _target_cpu
%ifarch x86_64
%define machine_arch %_target_cpu
%else
%define machine_arch i686
%endif
# machine_tmpl is the config template machine name, often "native"
%define machine_tmpl native
# machine is the actual machine name used in the dpdk make system
%ifarch x86_64
%define machine default
%endif
%ifarch i586
%define machine atm
%endif

%define target %machine_arch-%machine_tmpl-linuxapp-gcc

BuildRequires: kernel-headers, libpcap-devel, doxygen, python-module-sphinx, zlib-devel
BuildRequires: libnuma-devel
%if_with pdfdoc
BuildRequires: texlive-dejavu inkscape texlive-latex-bin-bin
BuildRequires: texlive-kpathsea-bin texlive-metafont-bin texlive-cm
BuildRequires: texlive-cmap texlive-ec texlive-babel-english
BuildRequires: texlive-fancyhdr texlive-fancybox texlive-titlesec
BuildRequires: texlive-framed texlive-threeparttable texlive-mdwtools
BuildRequires: texlive-wrapfig texlive-parskip texlive-upquote texlive-multirow
BuildRequires: texlive-helvetic texlive-times texlive-dvips
%endif

%description
The Data Plane Development Kit is a set of libraries and drivers for
fast packet processing in the user space.

%package devel
Summary: Data Plane Development Kit development files
Group: System/Libraries
Requires: %name%{?_isa} = %version-%release
%if_without shared
Provides: %name-static = %version-%release
%endif

%description devel
This package contains the headers and other files needed for developing
applications with the Data Plane Development Kit.

%if_with doc
%package doc
Summary: Data Plane Development Kit API documentation
Group: System/Libraries
BuildArch: noarch

%description doc
API programming documentation for the Data Plane Development Kit.
%endif

%if_with tools
%package tools
Summary: Tools for setting up Data Plane Development Kit environment
Group: Development/Documentation
Requires: %name = %version-%release
Requires: kmod pciutils findutils iproute

%description tools
%summary
%endif

%if_with examples
%package examples
Summary: Data Plane Development Kit example applications
Group: Development/Tools
BuildRequires: libvirt-devel

%description examples
Example applications utilizing the Data Plane Development Kit, such
as L2 and L3 forwarding.
%endif

%define sdkdir  %_libdir/%name
%define docdir  %_docdir/%name
%define incdir %_includedir/%name
%define pmddir %_libdir/%name-pmds

%prep
%setup
%patch0 -p2

%build
# set up a method for modifying the resulting .config file
function setconf() {
	if grep -q ^$1= %target/.config; then
		sed -i "s:^$1=.*$:$1=$2:g" %target/.config
	else
		echo $1=$2 >> %target/.config
	fi
}

# In case dpdk-devel is installed, we should ignore its hints about the SDK directories
unset RTE_SDK RTE_INCLUDE RTE_TARGET

# Avoid appending second -Wall to everything, it breaks upstream warning
# disablers in makefiles. Strip expclit -march= from optflags since they
# will only guarantee build failures, DPDK is picky with that.
export EXTRA_CFLAGS="$(echo %optflags | sed -e 's:-Wall::g' -e 's:-march=[[:alnum:]]* ::g') -Wformat -fPIC"

# DPDK defaults to using builder-specific compiler flags.  However,
# the config has been changed by specifying CONFIG_RTE_MACHINE=default
# in order to build for a more generic host.  NOTE: It is possible that
# the compiler flags used still won't work for all Fedora-supported
# machines, but runtime checks in DPDK will catch those situations.

make V=1 O=%target T=%target %{?_smp_mflags} config

setconf CONFIG_RTE_MACHINE '"%machine"'
# Disable experimental features
setconf CONFIG_RTE_NEXT_ABI n
setconf CONFIG_RTE_LIBRTE_CRYPTODEV n
setconf CONFIG_RTE_LIBRTE_MBUF_OFFLOAD n
# Disable unmaintained features
setconf CONFIG_RTE_LIBRTE_POWER n

# Enable automatic driver loading from this path
setconf CONFIG_RTE_EAL_PMD_PATH '"%pmddir"'

setconf CONFIG_RTE_LIBRTE_BNX2X_PMD y
setconf CONFIG_RTE_LIBRTE_PMD_PCAP y
setconf CONFIG_RTE_LIBRTE_VHOST_NUMA y

setconf CONFIG_RTE_EAL_IGB_UIO n
setconf CONFIG_RTE_LIBRTE_KNI n
setconf CONFIG_RTE_KNI_KMOD n
setconf CONFIG_RTE_KNI_PREEMPT_DEFAULT n

%if_with shared
setconf CONFIG_RTE_BUILD_SHARED_LIB y
%endif

make V=1 O=%target %{?_smp_mflags}
%if_with doc
make V=1 O=%target %{?_smp_mflags} doc-api-html doc-guides-html %{?with_pdfdoc: guides-pdf}
%endif

%if_with examples
make V=1 O=%target/examples T=%target %{?_smp_mflags} examples
%endif

%install
# In case dpdk-devel is installed
unset RTE_SDK RTE_INCLUDE RTE_TARGET

%makeinstall_std O=%target prefix=%_usr libdir=%_libdir

%if_without tools
rm -rf %buildroot%sdkdir/tools
rm -rf %buildroot%_sbindir/dpdk_nic_bind
%endif
rm -f %buildroot%sdkdir/tools/setup.sh

%if_with examples
find %target/examples/ -name "*.map" | xargs rm -f
for f in %target/examples/*/%target/app/*; do
    bn=`basename ${f}`
    cp -p ${f} %buildroot%_bindir/dpdk_example_${bn}
done
%endif

# Create a driver directory with symlinks to all pmds
mkdir -p %buildroot/%pmddir
for f in %buildroot/%_libdir/*_pmd_*.so; do
    bn=$(basename ${f})
    ln -s ../${bn} %buildroot%pmddir/${bn}
done

# Setup RTE_SDK environment as expected by apps etc
mkdir -p %buildroot/%_sysconfdir/profile.d
cat << EOF > %buildroot/%_sysconfdir/profile.d/dpdk-sdk-%_arch.sh
if [ -z "\${RTE_SDK}" ]; then
    export RTE_SDK="%sdkdir"
    export RTE_TARGET="%target"
    export RTE_INCLUDE="%incdir"
fi
EOF

cat << EOF > %buildroot/%_sysconfdir/profile.d/dpdk-sdk-%_arch.csh
if ( ! \$RTE_SDK ) then
    setenv RTE_SDK "%sdkdir"
    setenv RTE_TARGET "%target"
    setenv RTE_INCLUDE "%incdir"
endif
EOF

# Fixup target machine mismatch
%__subst 's:-%machine_tmpl-:-%machine-:g' %buildroot/%_sysconfdir/profile.d/dpdk-sdk*

%files
# BSD
%_bindir/testpmd
%_bindir/dpdk-procinfo
%if_with shared
%_libdir/*.so.*
%pmddir/
%endif

%if_with doc
%files doc
#BSD
%docdir
%endif

%files devel
#BSD
%incdir/
%sdkdir
%if_with tools
%exclude %sdkdir/tools/
%endif
%if_with examples
%exclude %sdkdir/examples/
%endif
%_sysconfdir/profile.d/dpdk-sdk-*.*
%if_without shared
%_libdir/*.a
%else
%_libdir/*.so
%endif

%if_with tools
%files tools
%sdkdir/tools/
%_sbindir/dpdk-devbind
%_bindir/dpdk-pdump
%_bindir/dpdk-pmdinfo
%endif

%if_with examples
%files examples
%_bindir/dpdk_example_*
%doc %sdkdir/examples
%endif

%changelog
* Thu Dec 08 2016 Lenar Shakirov <snejok@altlinux.ru> 16.11-alt1
- Initial build for ALT (based on 16.11-1.fc26.src)

