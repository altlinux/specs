Name:           cilium-envoy-cache
Version:        1.35.3
Release:        alt1
Summary:        Offline Bazel build cache for cilium-envoy

License:        Apache-2.0
Group:          Development/Tools
URL:            https://github.com/cilium/proxy

Source0:        bazel-cache.tar.gz

BuildArch:      noarch
ExcludeArch:    i586

%description
Offline Bazel dependencies (external/) and WORKSPACE fragment used to build cilium-envoy.

%install
mkdir -p %buildroot%_datadir/%name
install -m 0644 %SOURCE0 %buildroot%_datadir/%name/

%files
%_datadir/%name

%changelog
* Fri Nov 07 2025 Aleksandr Gamzin <gamzin@altlinux.org> 1.35.3-alt1
- Initial build for Sisyphus
