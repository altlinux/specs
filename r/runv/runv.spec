%def_without libvirt
%def_without xen

%global provider        github.com
%global project         hyperhq
%global repo            runv

%global provider_prefix %{provider}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          cc051a6f77fb678ca3c1609e8c1519bbfd858e60
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

Name:           runv
Version:        1.0.0
Release:        alt1.git.%shortcommit
Summary:        Open Container Initiative hypervisor-based runtime
Group:          Development/Other
License:        Apache 2.0
URL:            https://%provider_prefix
#ExclusiveArch:  %%go_arches
ExclusiveArch: x86_64 aarch64

Source0:        %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
%{?_with_libvirt:BuildRequires: libvirt-devel}
%{?_with_xen:BuildRequires: libxl-devel}

%description
Open Container Initiative hypervisor-based runtime.

runv is a command line client for running applications packaged according to
the Open Container Format (OCF) and is a compliant implementation of the
Open Container Initiative specification.  However, due to the difference
between hypervisors and containers, the following sections of OCF don't
apply to runV:
    Namespace
    Capability
    Device
    "linux" and "mount" fields in OCI specs are ignored

The current release of "runV" supports the following hypervisors:
    KVM (QEMU 2.0 or later)
    Xen (4.5 or later)
    VirtualBox (Mac OS X)

%prep
%setup -q

%build
#export GOPATH="%go_path"
#autoreconf
#configure --with-libvirt --without-xen
#make

export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .gopath/src/%import_path

export VERSION=%version
export COMMIT=%commit
export BRANCH=altlinux

export HYPER_BULD_TAGS="%{?_with_libvirt:with_libvirt} %{?_with_xen:with_xen}"

go build -i -tags "$HYPER_BULD_TAGS" -ldflags "-X main.version=$VERSION -X main.commit=$COMMIT -X main.branch=$BRANCH" -o runv ./cli/

%install
export BUILDDIR="$PWD/.gopath"
#export GOPATH="%go_path"

#%%golang_install

mkdir -p -- %buildroot%_bindir
install -p -m 755 $BUILDDIR/src/%import_path/runv %buildroot%_bindir

mkdir -p -- %buildroot%_tmpfilesdir
cat > %buildroot%_tmpfilesdir/%name.conf <<EOF
d /run/runv 0700 root root -
d /run/hyper 0700 root root -
EOF

# cleanup
rm -rf -- %buildroot%_datadir

%files
%doc NOTICE OWNERS README.md CONTRIBUTING.md docs/*.md
%_bindir/%name
%_tmpfilesdir/%name.conf

%changelog
* Thu Feb 01 2018 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1.git.cc051a6
- First build for Altlinux.
