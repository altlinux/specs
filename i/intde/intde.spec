Name: intde
Version: 1
Release: alt2
Summary: Numerical Automatic Integrator for Improper Integral
License: BSD
Group: Sciences/Mathematics
Url: http://crd.lbl.gov/~dhbailey/mpdist/

Source: %name-%version.tar

Requires: lib%name = %version-%release

BuildRequires: gcc-fortran gcc-c++

%description
Numerical Automatic Integrator for Improper Integral
  method    : Double Exponential (DE) Transformation
  dimension : one
routines
  intde  : integrator of f(x) over (a,b).
  intdei : integrator of f(x) over (a,infinity),
               f(x) is non oscillatory function.
  intdeo : integrator of f(x) over (a,infinity),
               f(x) is oscillatory function.

%package -n lib%name
Summary: Numerical Automatic Integrator for Improper Integral
Group: System/Libraries

%description -n lib%name
Numerical Automatic Integrator for Improper Integral
  method    : Double Exponential (DE) Transformation
  dimension : one
routines
  intde  : integrator of f(x) over (a,b).
  intdei : integrator of f(x) over (a,infinity),
               f(x) is non oscillatory function.
  intdeo : integrator of f(x) over (a,infinity),
               f(x) is oscillatory function.

%prep
%setup

%build
mkdir f
mv *.f f/
%add_optflags %optflags_shared

g++ -c *.c %optflags
pushd f
gfortran -c *.f %optflags
popd

mkdir t1 t2
mv *t.o t1/
mv f/*t.o t2/

for i in 1 2; do
	for j in '' f; do
g++ -shared *.o -Wl,-soname=lib%name$i$j.so \
	-o lib%name$i$j.so
	done
done

%install
install -d %buildroot%_libdir
install -m644 lib*.so %buildroot%_libdir/

%check
export LD_LIBRARY_PATH=$PWD
for i in t1/*.o t2/*.o; do
	g++ -o $i.out $i -L. -l%{name}1 -l%{name}1f -lgfortran
	echo test $i:
	./$i.out
done

%files -n lib%name
%doc *.txt
%_libdir/*.so
%doc *.doc *.c f/*.f

%changelog
* Tue Jan 23 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1-alt2
- Fixed build with new toolchain.

* Wed Sep 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1-alt1
- Initial build for Sisyphus

