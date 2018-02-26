Name: rpm-build-ocaml
Version: 1.1.1
Release: alt1
BuildArch: noarch

Summary: RPM helpers to rebuild OCaml packages
License: Public domain
Group: Development/ML
Packager: Alex V. Myltsev <avm@altlinux.ru>

Source: scripts-%version.tar

# for proper dependencies
BuildPreReq: rpm-build >= 4.0.4-alt81

Requires: %_bindir/ocamlrun
Requires: %_rpmlibdir/ocaml-reqprov

%description
RPM macros and reqprov helpers to be used in OCaml packages.

%prep
%setup -n scripts-%version

%install
mkdir -p %buildroot%_rpmlibdir
install -p -m755 ocaml.{req,prov}{.files,} ocaml-functions %buildroot%_rpmlibdir/

%files
%_rpmlibdir/ocaml*

%changelog
* Tue Apr 08 2008 Alexey Tourbin <at@altlinux.ru> 1.1.1-alt1
- ocaml.req: check "ccopt" libaray paths when resolving "cclib" dependencies

* Fri Apr 04 2008 Alexey Tourbin <at@altlinux.ru> 1.1-alt2
- added dependency on %_rpmlibdir/ocaml-reqprov

* Thu Apr 03 2008 Alexey Tourbin <at@altlinux.ru> 1.1-alt1
- major revision, implemented new types of dependencies:
  + ocaml-cmi(Unit) = V-hash - for bytecode units;
  + ocaml-cmx(Unit) = V-hash - for native units;
  + ocaml-dll(name) - for stub libraries (dll*.so);
  where V - major.minor of ocaml, hash - part of CRC

* Mon Jan 21 2007 Alex V. Myltsev <avm@altlinux.ru> 1-alt1
- Initial build for Sisyphus.

