Name: rpm-build-ocaml4
Version: 1.1.2
Release: alt2
BuildArch: noarch

Summary: RPM helpers to rebuild OCaml packages
License: Public domain
Group: Development/ML
Packager: %packager

Source: %name-%version.tar
Conflicts: rpm-build-ocaml

# for proper dependencies
BuildPreReq: rpm-build >= 4.0.4-alt81 

Requires: %_bindir/ocamlrun
Requires: %_rpmlibdir/ocaml-reqprov

%description
RPM macros and reqprov helpers to be used in OCaml packages.

%prep
%setup -q

%install
mkdir -p %buildroot%_rpmlibdir
install -p -m755 ocaml.{req,prov}{.files,} ocaml-functions %buildroot%_rpmlibdir/

%files
%_rpmlibdir/ocaml*

%changelog
* Sun Jun 19 2016 Andrey Bergman <vkni@altlinux.org> 1.1.2-alt2
- Rebuild with ocaml4 4.03.0.

* Tue Jun 30 2015 Andrey Bergman <vkni@altlinux.org> 1.1.2-alt1
- Corrected cmi required: skips dependencies if md5 sum is 0. This
is necessary for modules with C interfaces (C modules are
beyond the scope of rpm-build-ocaml4).

* Sun Jun 21 2015 Andrey Bergman <vkni@altlinux.org> 1.1.1-alt1
- Corrected ocaml- required/provides.

* Wed Oct 29 2014 Andrey Bergman <vkni@altlinux.org> 1.1.1-alt0.1
- Port to Ocaml4.

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

