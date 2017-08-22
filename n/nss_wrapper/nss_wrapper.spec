Name:           nss_wrapper
Version:        1.1.3
Release:        alt1
License:        BSD
Group:          Development/Other
Summary:        A wrapper for the user, group and hosts NSS API
Url:            https://cwrap.org/

# git://git.samba.org/nss_wrapper.git
Source0:        %{name}-%{version}.tar

BuildRequires:  cmake ctest
BuildRequires:  libcmocka-devel

Requires:       cmake
Requires:       pkgconfig

%description
There are projects which provide daemons needing to be able to create, modify
and delete Unix users. Or just switch user ids to interact with the system e.g.
a user space file server. To be able to test that you need the privilege to
modify the passwd and groups file. With nss_wrapper it is possible to define
your own passwd and groups file which will be used by software to act correctly
while under test.

If you have a client and server under test they normally use functions to
resolve network names to addresses (dns) or vice versa. The nss_wrappers allow
you to create a hosts file to setup name resolution for the addresses you use
with socket_wrapper.

To use it set the following environment variables:

LD_PRELOAD=libuid_wrapper.so
NSS_WRAPPER_PASSWD=/path/to/passwd
NSS_WRAPPER_GROUP=/path/to/group
NSS_WRAPPER_HOSTS=/path/to/host

This package doesn't have a devel package cause this project is for
development/testing.

%prep
%setup -q

%build
if test ! -e "obj"; then
    mkdir obj
fi

pushd obj
%cmake_insource \
  -DUNIT_TESTING=ON \
  %_builddir/%name-%version

%make VERBOSE=1
popd

%install
pushd obj
%make DESTDIR=%buildroot install
popd

%check
pushd obj
%make test
popd

%files
%doc AUTHORS README ChangeLog COPYING
%_bindir/nss_wrapper.pl
%_libdir/libnss_wrapper.so*
%dir %_libdir/cmake/nss_wrapper
%_libdir/cmake/nss_wrapper/nss_wrapper-config-version.cmake
%_libdir/cmake/nss_wrapper/nss_wrapper-config.cmake
%_libdir/pkgconfig/nss_wrapper.pc
%_mandir/man1/nss_wrapper.1*

%changelog
* Mon Aug 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.3-alt1
- Initial build for ALT.
