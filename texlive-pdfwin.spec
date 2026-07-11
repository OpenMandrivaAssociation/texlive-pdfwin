%global tl_name pdfwin
%global tl_revision 68667

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	customizable windows for screen viewing of TeX documents
Group:		Publishing
URL:		https://www.ctan.org/pkg/pdfwin
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfwin.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfwin.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Inspired by the pdfscreen package.

