%define oname dill
%def_with python3

Name:           python-module-%oname
Version:        0.2.7.1
Release:        alt1
Summary:        Serialize all of Python
Group:          Development/Python
License:        BSD
URL:            https://github.com/uqfoundation/dill
BuildArch:      noarch

# https://github.com/uqfoundation/dill.git
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
%endif

%description
Dill extends python's 'pickle' module for serializing and de-serializing
python objects to the majority of the built-in python types.
Dill provides the user the same interface as the 'pickle' module, and also
includes some additional features. In addition to pickling python objects, dill
provides the ability to save the state of an interpreter session in a single
command.

%if_with python3
%package -n python3-module-%oname
Summary: Serialize all of Python
Group: Development/Python3
%add_python3_req_skip __main__

%description -n python3-module-%oname
Dill extends python's 'pickle' module for serializing and de-serializing
python objects to the majority of the built-in python types.
Dill provides the user the same interface as the 'pickle' module, and also
includes some additional features. In addition to pickling python objects, dill
provides the ability to save the state of an interpreter session in a single
command.
%endif

%prep
%setup

%if_with python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif


%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc LICENSE README.md
%python_sitelibdir/%oname
%python_sitelibdir/%oname-%version-py?.?.egg-info

%files -n python3-module-%oname
%doc LICENSE README.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py?.?.egg-info

%changelog
* Fri Oct 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.7.1-alt1
- Initial build for ALT.

* Mon Sep 11 2017 Sergio Pascual <sergiopr@fedoraproject.org> - 0.2.7.1-2
- New upstream source (0.2.7.1)
- And the sources

* Tue Aug 08 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.6-3
- Fix %%python_provide invocation

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 16 2017 Sergio Pascual <sergiopr@fedoraproject.org> - 0.2.6-1
- New upstream source (0.2.6)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.5-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul 13 2016 Sergio Pascual <sergio.pasra@gmail.com> - 0.2.5-1
- New upstream source (0.2.5)
- Updated upstream url
- Pypi url updated

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 20 2015 Sergio Pascual <sergio.pasra@gmail.com> - 0.2.4-1
- New upstream source (0.2.4)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Sep 12 2014 Sergio Pascual <sergio.pasra@gmail.com> - 0.2.1-2
- Add license macro
- Run tests
- Add numpy build req for tests

* Thu Sep 11 2014 Sergio Pascual <sergio.pasra@gmail.com> - 0.2.1-1
- New upstream (0.2.1)

* Fri Dec 13 2013 Sergio Pascual <sergio.pasra@gmail.com> - 0.2-0.1b1
- Initial specfile
