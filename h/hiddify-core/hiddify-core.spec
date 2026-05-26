%define go_tags with_v2ray_api,with_gvisor,with_quic,with_dhcp,with_wireguard,with_utls,with_acme,with_clash_api,with_tailscale,with_ccm,with_ocm,tfogo_checklinkname0
%define gobuild go build -mod=vendor -tags=%go_tags

%define sover 0
%define libname libhiddify-core

# cd hiddify-sing-box && go run -v ./cmd/internal/read_tag --nightly
%define singbox_ver 1.13.1

Name:    hiddify-core
Version: 4.1.0
Release: alt1

Summary: Multi-platform, open-source, secure and ad-free auto-proxy client
License: GPLv3
Group:   Networking/Other

URL:     https://hiddify.com/
VCS:     https://github.com/hiddify/hiddify-core

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: %name-%version-hiddify-sing-box-replace-psiphon-quic-go.tar
Source3: %name-%version-hiddify-sing-box-replace-psiphon-tls.tar
Source4: %name-%version-hiddify-sing-box-replace-tailscale.tar
Source5: %name-%version-hiddify-sing-box-replace-wireguard-go.tar
Source6: %name-%version-hiddify-sing-box.tar
Source7: %name-%version-ray2sing.tar

Patch0: hiddify-core-4.1.0-alt-psiphon-tls-go-1.26.patch

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: /proc

%package -n hiddify-cli
Summary: Multi-platform, open-source, secure and ad-free auto-proxy client
Group:   Networking/Other

%package -n %libname%sover
Summary: Multi-platform, open-source, secure and ad-free auto-proxy client
Group:   Networking/Other

%package -n %libname-devel
Summary: Multi-platform, open-source, secure and ad-free auto-proxy client
Group:   Networking/Other

%define desc\
A powerful, high-performance core for the Hiddify ecosystem, supporting all\
major protocols and platforms.

%description %desc

%description -n hiddify-cli %desc
This package provides command line utility.

%description -n %libname%sover %desc
This package provides %name shared library.

%description -n %libname-devel %desc
This package provides %name development files.

%prep
%setup -a1 -a2 -a3 -a4 -a5 -a6 -a7
%patch0 -p1 -d ./vendor/github.com/Psiphon-Labs/psiphon-tls
%patch0 -p1 -d ./hiddify-sing-box/replace/psiphon-tls

%build
export GOROOT='%_libexecdir/golang'
export CGO_ENABLED=1
export CODE_VERSION="-X github.com/hiddify/hiddify-core/v2/hcommon/constants.Version=v%version -X github.com/sagernet/sing-box/constant.Version=%singbox_ver"

%gobuild \
	-buildmode=c-shared \
	-ldflags="$CODE_VERSION -extldflags -Wl,-soname,%libname.so.%sover" \
	-o=%libname.so.%sover \
	./platform/desktop

CGO_LDFLAGS='-L. -l:%libname.so.%sover' \
%gobuild -o=HiddifyCli ./cmd/bydll

%install
install -D ./%libname.so.%sover %buildroot%_libdir/%libname.so.%sover
install -D ./%libname.so.%sover %buildroot%_libdir/%libname.so
install -D ./%libname.so.h %buildroot%_includedir/hiddify-core.h
install -Dm755 ./HiddifyCli %buildroot%_bindir/HiddifyCli

%files -n hiddify-cli
%_bindir/HiddifyCli

%files -n %libname%sover
%_libdir/%libname.so.*

%files -n %libname-devel
%_libdir/%libname.so
%_includedir/hiddify-core.h

%changelog
* Tue May 26 2026 Ilya Sorochan <k0tran@altlinux.org> 4.1.0-alt1
- Initial build.
