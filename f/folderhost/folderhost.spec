%define _unpackaged_files_terminate_build 1
%define import_path github.com/MertJSX/folderhost

%ifarch %ix86 armh
%def_without aarch
%else
%def_with aarch
%endif

Name:    folderhost
Version: 26.6.1
Release: alt1

License: GPL-3.0
Group:   System/Servers
Summary: Your own private cloud in one executable
URL:     https://folderhost.org/
VCS:     https://github.com/MertJSX/folderhost

Source:  %name-%version.tar
Source1: vendor.tar
Source2: node_modules.tar
Source3: %name.service
Source4: %name.sysusers
Source5: %name.sysconfig

Patch1: folderhost-26.5.1-build_for_loongarch64_without_swc.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: rpm-build-nodejs

%if_with aarch
BuildRequires: rollup-native
BuildRequires: esbuild
%endif

ExcludeArch: %ix86

%description
Self-hosted cloud platform in a single binary.
Share files, collaborate in real-time,
and manage users with zero dependencies.

%prep
# Build the frontend assets.
# If building under aarch64, you need to update
# esbuild to the version current in sisyphus,
# and update @vitejs/plugin-react to a stable
# version, for example, 4.3.1:
# $ cd web
# $ npm install --no-save esbuild@actual_version \
#   @vitejs/plugin-react@4.3.1
# $ rm -rf node_modules/@vitejs/plugin-react-swc
# $ rm -rf node_modules/@swc
# $ rm -rf node_modules/vite/node_modules
# $ git add node_modules -f
# $ git commit -m "Update node js modules"
%setup -a 1 -a 2 -q
%patch1 -p1

%if_with aarch
# Use native rollup
mv node_modules/rollup node_modules/rollup.bak
cp -a %_prefix/lib/node_modules/rollup node_modules
cp -a %_prefix/lib/node_modules/@rollup/rollup-*-gnu node_modules/@rollup
%endif

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOFLAGS="-mod=vendor"
export GOROOT="%_libexecdir/golang"

%golang_prepare
# Building app
pushd web
%if_with aarch
# Use system esbuild. Note that /usr/bin/esbuild cannot be used
# because eslint module specifically checks for such path.
ESBUILD_BINARY_PATH=/bin/esbuild npm run build
%else
npm run build
%endif
popd

%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
export GOROOT="%_libexecdir/golang"
mkdir -p %buildroot%_datadir/%name

%golang_install
mkdir -p %buildroot%_unitdir
mkdir -p %buildroot%_sysusersdir
mkdir -p %buildroot%_sysconfdir/sysconfig
mkdir -p %buildroot%_sysconfdir/%name
mkdir -p %buildroot%_sharedstatedir/%name

install -Dm 0644 resources/default_config.yml \
 %buildroot%_sysconfdir/%name/config.yml.example
install -Dm 0644 resources/default_services.yml \
 %buildroot%_sysconfdir/%name/services.yml.example

install -Dm 0644 %SOURCE3 %buildroot%_unitdir/%name.service
install -Dm 0644 %SOURCE4 %buildroot%_sysusersdir/%name.conf
install -Dm 0600 %SOURCE5 %buildroot%_sysconfdir/sysconfig/%name

%pre
%sysusers_create_package %name %SOURCE4

%post
%post_service %name

%preun
%preun_service %name

%files
%doc LICENSE README.*
%_bindir/%name
%_unitdir/%name.service
%_sysusersdir/%name.conf
%config(noreplace) %attr(0640, root, _folderhost) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/%name/config.yml.example
%config(noreplace) %_sysconfdir/%name/services.yml.example
%dir %_sysconfdir/%name
%dir %attr(0750, _%name, _%name) %_sharedstatedir/%name

%changelog
* Fri Jun 26 2026 Sergey Savelev <medovi@altlinux.org> 26.6.1-alt1
- New version 26.6.1.

* Thu Jun 25 2026 Sergey Savelev <medovi@altlinux.org> 26.6.0-alt1
- New version 26.6.0.

* Tue Jun 02 2026 Sergey Savelev <medovi@altlinux.org> 26.5.1-alt1
- Initial build for Sisyphus.
