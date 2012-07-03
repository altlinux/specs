%define path_to_mpihome %_libexecdir/mpitests
%define test_home %path_to_mpihome/tests
%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl

Summary: MPI Benchmarks and tests
Name: mpitests
Version: 3.2
Release: alt3
License: BSD
Group: Networking/Other
Source: %name-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
URL: http://www.openfabrics.org/

BuildPreReq: %mpiimpl-devel chrpath

%description
Set of popular MPI benchmarks:
IMB-3.2
Presta-1.4.0
OSU benchmarks ver 3.1.1

%prep
%setup

%build
export PATH=$PATH:%mpidir/bin
%make_build MPIHOME=%mpidir

mv osu_benchmarks-3.1.1/README README_osu_benchmarks
mv presta-1.4.0/README README_presta

%install
%make_install MPIHOME=%buildroot%_libexecdir install

for i in %buildroot%_libexecdir/mpitests/*/*
do
	chrpath -r %mpidir/lib $i ||:
done

%files 
%doc IMB-3.2/doc/* README*
%_libexecdir/%name

%changelog
* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt3
- Fixed RPATH

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt2
- Rebuilt for debuginfo

* Fri Aug 13 2010 Andriy Stepanov <stanv@altlinux.ru> 3.2-alt1
- New version.

* Mon May 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt1
- Initial build for Sisyphus

* Thu Oct  2 2008 Pavel Shamis (pasha@mellanox.co.il)
  Intel MPI benchmark IMB-3.0 was updated to IMB-3.1
* Thu Nov 22 2006 Pavel Shamis (pasha@mellanox.co.il)
  Intel MPI benchmark IMB-2.3 was updated to IMB-3.0
  OSU benchmarks were updated from 2.0 to 3.0
  mpitest package version updated from 2.0 to 3.0
  removing old code from spec
* Tue Jun 20 2006 Pavel Shamis (pasha@mellanox.co.il)
  Pallas benchmark 2.2.1 was replaced with Intel MPI benchmark IMB-2.3
  Presta 1.2 was updated to 1.4.0
  OSU benchmarks were updated from 1.0 to 2.0
  mpitest package version updated from 1.0 to 2.0
* Wed Apr 01 2006 Pavel Shamis (pasha@mellanox.co.il)
  Spec file for mpitests was created.
