Name:           qcl
Version:        0.6.4
Release:        alt2
Summary:        Quantum Computation Language with an emulator of a quantum computer
License:        GPLv2
URL:            http://tph.tuwien.ac.at/~oemer/qcl.html
Group:          Sciences/Physics

Source0:        %name-%version.tar
Source1:        ccquprog.pdf
Source2:        qcldoc.pdf
Source3:		quprog.pdf
Source4:		structquprog.pdf

BuildRequires:  gcc-c++ bison flex
BuildRequires:  libplotter-devel libreadline-devel libncurses-devel

%description
QCL is a high level, architecture independent programming language for quantum
computers, with a syntax derived from classical procedural languages like C or
Pascal. This allows for the complete implementation and simulation of quantum
algorithms (including classical components) in one consistent formalism.

%package        doc
Summary:        Provides comprehensive documentation for the QCL
Group:          Sciences/Physics
Requires:       %name = %version-%release

%description    doc
Comprehensive PDF documentation for the Quantum Computation Language with an
emulator of a quantum computer.

%prep
%setup -q

%build
export CXXFLAGS="%optflags"
%make_build

%install
install -m 0755 -d %buildroot%_bindir %buildroot%_libexecdir/%name
install -m 0755 ./qcl %buildroot%_bindir
install -m 0644 ./lib/*.qcl %buildroot%_libexecdir/%name

mkdir -p %buildroot%_docdir
cp %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4 %buildroot%_docdir

%files
%doc CHANGES README
%_bindir/qcl
%_libexecdir/qcl/*

%files doc
%_docdir/*.pdf

%changelog
* Thu Jan 31 2019 Andrew Savchenko <bircoph@altlinux.org> 0.6.4-alt2
- Fix QCL libdir.

* Thu Jan 31 2019 Andrew Savchenko <bircoph@altlinux.org> 0.6.4-alt1
- Initial release
