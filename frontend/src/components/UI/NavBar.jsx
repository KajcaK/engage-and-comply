import {Container, Nav, Navbar} from "react-bootstrap";
import {Icon} from "@iconify/react";

const NavBar = () => (
    <Navbar expand="lg" bg="dark" variant="dark" className="navbar-container">
        <Container fluid>
            <Navbar.Brand href="/" className="d-flex align-items-center text-white text-decoration-none fs-4 ms-3">
                A.C.E. - AI for Compliant Engagement
            </Navbar.Brand>
            <Navbar.Toggle aria-controls="app-navbar" className="glow-button"/>
            <Navbar.Collapse id="app-navbar" className="bg-dark navbar-collapse z-3">
                <Nav className="ms-auto me-5 my-2 justify-content-center align-items-center ">
                    <Nav.Link href="/" className="me-1">
                        <Icon icon="eos-icons:machine-learning-outlined" width="26" height="26" className="me-1 mb-1"/>
                        Chat
                    </Nav.Link>
                    <Nav.Link href="/upload-link">
                        <Icon icon="flowbite:link-outline" width="26" height="26" className="me-1 mb-1"/>
                        Upload Link
                    </Nav.Link>
                    <Nav.Link href="/upload-pdf">
                        <Icon icon="ant-design:file-pdf-outlined" width="26" height="26" className="me-1 mb-1"/>
                        Upload PDF
                    </Nav.Link>
                </Nav>
            </Navbar.Collapse>
        </Container>
    </Navbar>
);

export default NavBar