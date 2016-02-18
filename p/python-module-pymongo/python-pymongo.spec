# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-build-python3 rpm-macros-fedora-compat
# END SourceDeps(oneline)
%define oldname python-pymongo
%define fedora 21
%if 0%{?fedora} > 17
%global with_python3 1
%else
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%endif

# don't try connect to the server:
%def_disable check

# Fix private-shared-object-provides error
%{echo 


}

Name:           python-module-pymongo
Version:        3.0.3
Release:        alt1.1
Summary:        Python driver for MongoDB

Group:          Development/Python
# All code is ASL 2.0 except bson/time64*.{c,h} which is MIT
License:        ASL 2.0 and MIT
URL:            http://api.mongodb.org/python
Source0:        http://pypi.python.org/packages/source/p/pymongo/pymongo-%{version}.tar.gz

Provides:       pymongo = %{version}-%{release}
Obsoletes:      pymongo <= 2.1.1-4

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-2to3 python3 python3-base
BuildRequires: python-module-nose python3-devel python3-module-setuptools rpm-build-python3 time

#BuildRequires:  python-devel
#BuildRequires:  python-module-nose
#BuildRequires:  python-module-setuptools

%if 0%{?with_python3}
#BuildRequires: python-tools-2to3 python-tools-i18n python-tools-idle python-tools-pynche python-tools-smtpd
#BuildRequires:  python3-devel
#BuildRequires:  python3-module-distribute
%endif # if with_python3

# Mongodb must run on a little-endian CPU (see bug #630898)
ExcludeArch:    ppc ppc64  s390 s390x
Source44: import.info
%add_findprov_skiplist %{python_sitelibdir}.*\.so$

%description
The Python driver for MongoDB.

%if 0%{?with_python3}
%package -n python3-module-pymongo
Summary:        Python driver for MongoDB
Group:          Development/Python3
Requires:       python3-module-bson = %{version}-%{release}

%description -n python3-module-pymongo
The Python driver for MongoDB.  This package contains the python3 version of
this module.
%endif # with_python3

%package -n python-module-pymongo-gridfs
Summary:        Python GridFS driver for MongoDB
Group:          Development/Python
Provides:       pymongo-gridfs = %{version}-%{release}
Obsoletes:      pymongo-gridfs <= 2.1.1-4

%description -n python-module-pymongo-gridfs
GridFS is a storage specification for large objects in MongoDB.

%if 0%{?with_python3}
%package -n python3-module-gridfs
Summary:        Python GridFS driver for MongoDB
Group:          Development/Python3
Requires:       python3-module-pymongo = %{version}-%{release}

%description -n python3-module-gridfs
GridFS is a storage specification for large objects in MongoDB.  This package
contains the python3 version of this module.
%endif # with_python3

%package -n python-module-bson
Summary:        Python bson library
Group:          Development/Python

%description -n python-module-bson
BSON is a binary-encoded serialization of JSON-like documents. BSON is designed
to be lightweight, traversable, and efficient. BSON, like JSON, supports the
embedding of objects and arrays within other objects and arrays.

%if 0%{?with_python3}
%package -n python3-module-bson
Summary:        Python bson library
Group:          Development/Python3

%description -n python3-module-bson
BSON is a binary-encoded serialization of JSON-like documents. BSON is designed
to be lightweight, traversable, and efficient. BSON, like JSON, supports the
embedding of objects and arrays within other objects and arrays.  This package
contains the python3 version of this module.
%endif # with_python3

%prep
%setup -q -n pymongo-%{version}
rm -r pymongo.egg-info

%if 0%{?with_python3}
rm -rf %{_builddir}/python3-%{oldname}-%{version}-%{release}
cp -a . %{_builddir}/python3-%{oldname}-%{version}-%{release}
2to3 --write --nobackups --no-diffs %{_builddir}/python3-%{oldname}-%{version}-%{release}
%endif # with_python3

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%if 0%{?with_python3}
pushd %{_builddir}/python3-%{oldname}-%{version}-%{release}
CFLAGS="%{optflags}" %{__python3} setup.py build
popd
%endif # with_python3

%install
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

%if 0%{?with_python3}
pushd %{_builddir}/python3-%{oldname}-%{version}-%{release}
%{__python3} setup.py install --skip-build --root $RPM_BUILD_ROOT
popd
%endif # with_python3

%files
%doc LICENSE PKG-INFO README.rst doc
%{python_sitelibdir}/pymongo
%{python_sitelibdir}/pymongo-%{version}-*.egg-info

%if 0%{?with_python3}
%files -n python3-module-pymongo
%doc LICENSE PKG-INFO README.rst doc
%{python3_sitelibdir}/pymongo
%{python3_sitelibdir}/pymongo-%{version}-*.egg-info
%endif # with_python3

%files -n python-module-pymongo-gridfs
%doc LICENSE PKG-INFO README.rst doc
%{python_sitelibdir}/gridfs

%if 0%{?with_python3}
%files -n python3-module-gridfs
%doc LICENSE PKG-INFO README.rst doc
%{python3_sitelibdir}/gridfs
%endif # with_python3

%files -n python-module-bson
%doc LICENSE PKG-INFO README.rst doc
%{python_sitelibdir}/bson

%if 0%{?with_python3}
%files -n python3-module-bson
%doc LICENSE PKG-INFO README.rst doc
%{python3_sitelibdir}/bson
%endif # with_python3

%check
# Exclude tests that require an active MongoDB connection
 exclude='(^test_auth_from_uri$'
exclude+='|^test_auto_auth_login$'
exclude+='|^test_auto_reconnect_exception_when_read_preference_is_secondary$'
exclude+='|^test_auto_start_request$'
exclude+='|^test_binary$'
exclude+='|^test_client$'
exclude+='|^test_collection$'
exclude+='|^test_common$'
exclude+='|^test_config_ssl$'
exclude+='|^test_connect$'
exclude+='|^test_connection$'
exclude+='|^test_constants$'
exclude+='|^test_contextlib$'
exclude+='|^test_copy_db$'
exclude+='|^test_cursor$'
exclude+='|^test_database$'
exclude+='|^test_database_names$'
exclude+='|^test_delegated_auth$'
exclude+='|^test_disconnect$'
exclude+='|^test_document_class$'
exclude+='|^test_drop_database$'
exclude+='|^test_equality$'
exclude+='|^test_fork$'
exclude+='|^test_from_uri$'
exclude+='|^test_fsync_lock_unlock$'
exclude+='|^test_get_db$'
exclude+='|^test_getters$'
exclude+='|^test_grid_file$'
exclude+='|^test_gridfs$'
exclude+='|^test_host_w_port$'
exclude+='|^test_interrupt_signal$'
exclude+='|^test_ipv6$'
exclude+='|^test_iteration$'
exclude+='|^test_json_util$'
exclude+='|^test_kill_cursor_explicit_primary$'
exclude+='|^test_kill_cursor_explicit_secondary$'
exclude+='|^test_master_slave_connection$'
exclude+='|^test_nested_request$'
exclude+='|^test_network_timeout$'
exclude+='|^test_network_timeout_validation$'
exclude+='|^test_operation_failure_with_request$'
exclude+='|^test_operation_failure_without_request$'
exclude+='|^test_operations$'
exclude+='|^test_pinned_member$'
exclude+='|^test_pooling$'
exclude+='|^test_pooling_gevent$'
exclude+='|^test_properties$'
exclude+='|^test_pymongo$'
exclude+='|^test_read_preferences$'
exclude+='|^test_replica_set_client$'
exclude+='|^test_replica_set_connection$'
exclude+='|^test_replica_set_connection_alias$'
exclude+='|^test_repr$'
exclude+='|^test_request_threads$'
exclude+='|^test_safe_insert$'
exclude+='|^test_safe_update$'
exclude+='|^test_schedule_refresh$'
exclude+='|^test_server_disconnect$'
exclude+='|^test_son_manipulator$'
exclude+='|^test_threading$'
exclude+='|^test_threads$'
exclude+='|^test_threads_replica_set_connection$'
exclude+='|^test_timeouts$'
exclude+='|^test_tz_aware$'
exclude+='|^test_uri_options$'
exclude+='|^test_use_greenlets$'
exclude+='|^test_with_start_request$'
exclude+=')'
pushd test
nosetests --exclude="$exclude"
popd

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.0.3-alt1.1
- NMU: Use buildreq for BR.

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt1
- Version 3.0.3

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.2-alt1
- Version 2.7.2

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt1_6
- update to new release by fcimport

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt1_5
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt1_4
- update to new release by fcimport

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt1_3
- new version

* Sat Mar 23 2013 Aleksey Avdeev <solo@altlinux.ru> 2.3-alt2.1
- Rebuild with Python-3.3

* Wed Jan 09 2013 Igor Vlasenko <viy@altlinux.ru> 2.3-alt2
- 2.3

* Sun Jan 06 2013 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_5
- fc import

* Wed May 02 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2-alt1
- 2.2
- Build with Python3 support

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.1-alt1.1
- Rebuild with Python-2.7

* Mon Sep 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Wed Jul 21 2010 Egor Glukhov <kaman@altlinux.org> 1.7-alt1
- Initial build for Sisyphus
