Name:    libdnf
Version: 0.60.0
Release: alt2

Summary: Package management library.
License: LGPL-2.1
Group:   System/Libraries
Url:     https://github.com/rpm-software-management/libdnf

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: libcheck-devel
BuildRequires: libgio-devel
BuildRequires: libjson-c-devel
BuildRequires: libmodulemd-devel
BuildRequires: librepo-devel
BuildRequires: librpm-devel
BuildRequires: libsolv-devel
BuildRequires: libssl-devel
BuildRequires: libsmartcols-devel
BuildRequires: libsqlite3-devel
BuildRequires: python3-dev
BuildRequires: swig
BuildRequires: python3-module-sphinx
BuildRequires: cppunit-devel
BuildRequires: libgpgme-devel

%description
This library provides a high level package-manager. It's core library of dnf,
PackageKit and rpm-ostree. It's replacement for deprecated hawkey library which
it contains inside and uses librepo under the hood.

%package devel
Summary: Development files for %name
Group: Development/C++

%description devel
%{summary}.

%package -n python3-module-libdnf
Summary: Python3 API to %name
Group: Development/Python3

%description -n python3-module-libdnf
Python3 API to %{name}.

%package -n python3-module-hawkey
Summary: Python 3 bindings for the hawkey library
Group: Development/Python3

%description -n python3-module-hawkey
Python3 bindings for the hawkey library.

%prep
%setup
%ifarch %e2k
# workaround for EDG frontend
find libdnf tests -name '*.cpp' | xargs sed -i "\
  s|g_autofree gchar \*|g_autofree_edg(gchar) |;\
  s|g_autofree char \*|g_autofree_edg(char) |"

sed -i "s/g_object_ref(repo)/g_object_ref((DnfRepo*)repo)/" \
	libdnf/dnf-repo-loader.cpp

sed -i "s/auto it = keys;/auto it = (GStrv)keys;/;\
  s/string::trim(str)/string::trim((gchar*)str)/;\
  s/REPOCONFIG, tmp_strval/REPOCONFIG, (gchar*)tmp_strval/" \
	libdnf/dnf-repo.cpp

cat >> libdnf/hy-query.h << "EOF"
#if defined(hy_autoquery) && defined(__cplusplus)
#undef hy_autoquery
class HyQuery_auto {
  HyQuery v;
  HyQuery_auto(HyQuery_auto &x) { v = (HyQuery)x; }
public:
  HyQuery_auto(const HyQuery_auto &x) { v = (HyQuery)x; }
  HyQuery_auto(HyQuery x) { v = x; }
  ~HyQuery_auto() { hy_query_autofree(&v); }
	HyQuery operator->() { return v; } \
  HyQuery operator=(HyQuery x) { return (v = x); }
  operator HyQuery() const { return v; }
};
#endif
EOF
sed -i "s/hy_autoquery HyQuery /HyQuery_auto /" \
	libdnf/dnf-context.cpp
sed -i '/arch_map\[\] =/a {"e2k",{"e2k","e2kv3","e2kv4","e2kv5","e2kv6",NULL}},' \
	libdnf/dnf-context.cpp

sed -i "s/parser.read(cfn)/parser.read((gchar*)cfn)/;\
  s/filesystem::getDirContent(dirPath)/filesystem::getDirContent((gchar*)dirPath)/;\
  /try {/{n;s/getFileContent(file)/getFileContent(std::string((gchar*)file))/}" \
	libdnf/module/ModulePackageContainer.cpp
%endif

%build
%cmake -GNinja \
       -Wno-dev \
       -DWITH_ZCHUNK=OFF \
       -DWITH_GTKDOC=OFF \
       -DWITH_HTML=OFF \
       -DWITH_MAN=ON
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"
%find_lang %name
rm -rf %buildroot%python3_sitelibdir/hawkey/test/

%files -f %name.lang
%doc AUTHORS README.md
%_libdir/*.so.*
%dir %_libdir/%name/plugins/
%doc %_libdir/%name/plugins/README

%files devel
%_libdir/*.so
%_includedir/%name
%_libdir/pkgconfig/*.pc

%files -n python3-module-libdnf
%python3_sitelibdir/%name

%files -n python3-module-hawkey
%python3_sitelibdir/hawkey
%_man3dir/hawkey.3*

%changelog
* Thu Nov 17 2022 Michael Shigorin <mike@altlinux.org> 0.60.0-alt2
- Fixes for Elbrus build (ilyakurdyukov@).

* Mon Oct 31 2022 Andrey Cherepanov <cas@altlinux.org> 0.60.0-alt1
- Initial build for Sisyphus.
