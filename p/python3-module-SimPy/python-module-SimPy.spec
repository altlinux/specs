%define oname SimPy
%define major 3.0

Name: python3-module-%oname
Version: %major.11
Release: alt1

Summary: SimPy simulation package
License: LGPL
Group: Development/Python3
Url: http://simpy.sourceforge.net/
BuildArch: noarch

Source: http://sourceforge.net/projects/simpy/files/simpy/SimPy-%major/%oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools


%description
SimPy is a process-based discrete-event simulation language
based on standard Python and released under the GNU LGPL.

It provides the modeller with components of a simulation
model. These include processes, for active components like
customers, messages, and vehicles, and resources, for
passive components that form limited capacity congestion
points like servers, checkout counters, and tunnels. It
also provides monitor variables to aid in gathering
statistics. SimPy comes with extensive plotting capabilities.

The distribution contains in-depth documentation, tutorials,
and a large number of simulation models.

Simulation model developers are encouraged to share their
SimPy modeling techniques with the SimPy community. Please
post a message to the simpy-Users mailing list,

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc CHANGES.txt AUTHORS.txt LICENSE.txt README.txt
%python3_sitelibdir/*


%changelog
* Tue Oct 22 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.0.11-alt1
- Version updated to 3.0.11
- python2 -> python3

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 2.3.1-alt1
- new version 2.3.1 (with rpmrb script)
- cleanup spec

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8-alt2.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.8-alt1.1
- Rebuilt with python-2.5.

* Sun Oct 28 2007 Vitaly Lipatov <lav@altlinux.ru> 1.8-alt1
- initial build for ALT Linux Sisyphus
