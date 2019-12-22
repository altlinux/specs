Name: libkafel
Version: 1
Release: alt3.git8e69b8e

Summary: A language and library for specifying syscall filtering policies
License: Apache-2.0
Group: System/Libraries
Url: https://github.com/google/kafel

Packager: Alexey Gladkov <legion@altlinux.ru>

Source0: %name-%version.tar

ExcludeArch: ppc64le

BuildRequires: flex

%description
Kafel is a language and library for specifying syscall filtering policies.
The policies are compiled into BPF code that can be used with seccomp-filter.

%package devel
Summary: This package contains development files of %name
Group: Development/C

%description devel
%summary


%prep
%setup -q

sed -i -e 's#-soname,$@#-soname,$(notdir $@)#' src/Makefile


%build
make


%install
mkdir -p -- %buildroot/%_libdir
cp -a -- libkafel.so       %buildroot/%_libdir/libkafel.so.1.0.0
ln -s -- libkafel.so.1.0.0 %buildroot/%_libdir/libkafel.so

mkdir -p -- %buildroot/%_includedir
cp -a -- include/*.h   %buildroot/%_includedir/


%files
%_libdir/libkafel.so.*


%files devel
%_includedir/*.h
%_libdir/libkafel.so


%changelog
* Sun Dec 22 2019 Alexey Gladkov <legion@altlinux.ru> 1-alt3.git8e69b8e
- New snapshot.

* Thu Jul 05 2018 Alexey Gladkov <legion@altlinux.ru> 1-alt2.git409ccb2
- New snapshot.

* Fri Apr 06 2018 Alexey Gladkov <legion@altlinux.ru> 1-alt1.gitf664aca
- First build.
