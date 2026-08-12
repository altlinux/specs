# Bootstrap knob (default: WITH). Normal builds include the OCaml
# ocaml-meta-reqprov binary; `rpmbuild --without ocaml_meta` drops it (and the
# ocaml/findlib BuildRequires) to break the ocaml <-> rpm-build-ocaml build
# cycle. The %%{?!_without_ocaml_meta:...} guards below implement the switch.
%def_with ocaml_meta

Name: rpm-build-ocaml
Version: 1.7.0
Release: alt1
Summary: RPM helpers to rebuild OCaml packages
License: GPL-2.0-or-later
Group: Development/ML
Url: https://git.altlinux.org/gears/r/rpm-build-ocaml.git
VCS: https://git.altlinux.org/gears/r/rpm-build-ocaml.git

Source: %name-%version.tar

# for proper dependencies
BuildPreReq: rpm-build >= 4.0.4-alt81
BuildRequires: rpm-macros-ocaml-version
%{?!_without_ocaml_meta:BuildRequires: ocaml ocaml-findlib-devel}

# ocaml-reqprov lives in ocaml-runtime, which also ships %_bindir/ocamlrun,
# so an explicit Requires on ocamlrun is redundant.
Requires: %_rpmlibdir/ocaml-reqprov
Requires: rpm-macros-ocaml-version
Obsoletes: rpm-build-ocaml4

%description
RPM macros and reqprov helpers to be used in OCaml packages.

%prep
%setup

%build
subst 's/@ocamlsver@/%{ocaml_version}/' scripts/ocaml
%{?!_without_ocaml_meta:make}

%install
mkdir -p %buildroot%_rpmlibdir
install -pD -m644 scripts/ocaml %buildroot%_rpmmacrosdir/ocaml
install -pD -m644 scripts/ocaml.env %buildroot%_rpmmacrosdir/ocaml.env
install -p -m755 scripts/ocaml.{req,prov}{.files,} scripts/ocaml-functions scripts/ocaml-find-files-multi %buildroot%_rpmlibdir/
%{?!_without_ocaml_meta:install -p -m755 ocaml-meta-reqprov %buildroot%_rpmlibdir/}

%files
%_rpmmacrosdir/ocaml
%_rpmmacrosdir/ocaml.env
%_rpmlibdir/ocaml*

%changelog
* Thu Apr 09 2026 Anton Farygin <rider@altlinux.ru> 1.7.0-alt1
- added ocaml-meta() Provides/Requires generation from META files
  using Fl_metascanner.lookup with predicate-aware resolution
- moved META from devel to runtime package for findlib support
- ocaml-meta-reqprov built as standalone ELF (-output-complete-exe)
- dropped ocaml-cmt() Provides/Requires generation: redundant with
  ocaml-cmx() for native packages; .cmt/.cmti still shipped for tooling
- route C stub static archives (lib*.a) to the runtime package next to
  their dll*.so, so -output-complete-exe / -custom static linking finds
  them via the already-pulled runtime dep; OCaml native .a stay in devel
- move dune-package to the runtime package next to META: it is dune's
  library-resolution metadata (like findlib META), so building against a
  library with dune works with only its runtime installed (the ocaml-meta
  graph then pulls the whole transitive dune-package closure)
- honor findlib exists_if in ocaml-meta-reqprov: skip META subpackages whose
  guard file is absent (e.g. topkg's `care` subpackage under ../topkg-care
  when only topkg is built), so we stop emitting false ocaml-meta() provides
  and spurious requires for subpackages that were not installed
- skip requires guarded by toploop/create_toploop/syntax/preprocessor
  predicates: these are toplevel- or camlp4/camlp5-only deps, not general
  package requires (avoids over-pulling camlp5 onto every consumer)
- honor an explicit findlib `name = "..."` for the root Provides name

* Thu Mar 05 2026 Anton Farygin <rider@altlinux.org> 1.6.7-alt1
- renamed %%ocaml_bootstrap -> %%_with_ocaml_bootstrap to use in %%if_with macro

* Tue Mar 03 2026 Anton Farygin <rider@altlinux.org> 1.6.6-alt1
- added %%ocaml_bootstrap macros

* Thu Dec 26 2025 Anton Farygin <rider@altlinux.ru> 1.6.5-alt1
- added %%ocaml_find_files_multi and %%dune_install_multi macros
  for multi-package dune projects (e.g., opam, dune)
- generates per-package file listings: ocaml-files.runtime.<pkg>,
  ocaml-files.devel.<pkg>
- uses .install files from _build when available for accurate file lists

* Mon Jan 20 2025 Anton Farygin <rider@altlinux.ru> 1.6.4-alt1
- enabled parallel build in Dune with %%_smp_mflags
- remove ocaml-cmi dependencies for .cmt and .cmti files in devel packages
- refined OCaml packaging logic to accurately include/exclude relevant files
- moved .cma and .cmi files to the devel package and .cmo files to the runtime
  package to ensure proper separation
- move META file to the devel package as it is used only during development for
  dependency resolution and library configuration, not needed at runtime

* Tue Sep 03 2024 Anton Farygin <rider@altlinux.ru> 1.6.3-alt1
- provide (in addition to implementation) version for interface (ocaml-cmi)
  from .cmx files

* Thu Apr 25 2024 Arseny Maslennikov <arseny@altlinux.org> 1.6.2.1-alt1
- Stopped using files packaged in the rpm project.

* Wed Nov 22 2023 Anton Farygin <rider@altlinux.ru> 1.6.2-alt1
- fixed removal of the dependencies for ocaml symbols without a
  hash information from the modules

* Sun Nov 19 2023 Anton Farygin <rider@altlinux.ru> 1.6.1-alt1
- added cmt and cmti files to requires and provides tracking

* Wed Nov 15 2023 Anton Farygin <rider@altlinux.ru> 1.6.0-alt1
- added %%ocaml_native_arch and %%ocaml_find_files

* Wed Nov 08 2023 Anton Farygin <rider@altlinux.ru> 1.5.0-alt1
- added .o and .cmo files to filelist of the devel package in
  dune_install macros

* Sun Apr 04 2021 Anton Farygin <rider@altlinux.org> 1.4.2-alt1
- removed the creation of buggy dependencies from .cmxa to .a archives
  (ocaml 4.12 does not create .a archive for the empty cmxa)

* Sun Dec 06 2020 Anton Farygin <rider@altlinux.ru> 1.4.1-alt1
- require full version of the ocaml-runtime
- relaxed the text relocations check for 32-bit x86 and armh architectures

* Fri Sep 11 2020 Anton Farygin <rider@altlinux.ru> 1.4-alt1
- %%ocamldir renamed to %%_ocamldir
- added %%dune_build, %%dune_install and %%dune_check
- removed conflict with ocaml4-runtime

* Tue May 16 2017 Anton Farygin <rider@altlinux.ru> 1.3-alt1
- added %%add_ocaml_req_skip macros
- added %%ocamldir

* Tue Apr 18 2017 Anton Farygin <rider@altlinux.ru> 1.2-alt1
- added stublibs path to search shared libraries in cmxi archives
- resolve .so path for avoid requires to devel packages in runtime ocaml libraries

* Thu Feb 16 2017 Anton Farygin <rider@altlinux.ru> 1.1.1-alt2
- added temporaty conflict with ocaml4-runtime

* Tue Apr 08 2008 Alexey Tourbin <at@altlinux.ru> 1.1.1-alt1
- ocaml.req: check "ccopt" libaray paths when resolving "cclib" dependencies

* Fri Apr 04 2008 Alexey Tourbin <at@altlinux.ru> 1.1-alt2
- added dependency on %%_rpmlibdir/ocaml-reqprov

* Thu Apr 03 2008 Alexey Tourbin <at@altlinux.ru> 1.1-alt1
- major revision, implemented new types of dependencies:
  + ocaml-cmi(Unit) = V-hash - for bytecode units;
  + ocaml-cmx(Unit) = V-hash - for native units;
  + ocaml-dll(name) - for stub libraries (dll*.so);
  where V - major.minor of ocaml, hash - part of CRC

* Mon Jan 21 2007 Alex V. Myltsev <avm@altlinux.ru> 1-alt1
- Initial build for Sisyphus.
